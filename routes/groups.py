from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models import Group, GroupMember, User, Recipe, GroupInvitation
import cloudinary.uploader

groups_bp = Blueprint('groups', __name__)

@groups_bp.route('', methods=['GET'])
def get_all_groups():
    groups = Group.query.all()
    return jsonify([group.to_dict() for group in groups]), 200

@groups_bp.route('/my-groups', methods=['GET'])
@jwt_required()
def get_my_groups():
    user_id = int(get_jwt_identity())
    created_groups = Group.query.filter_by(created_by=user_id).all()
    memberships = GroupMember.query.filter_by(user_id=user_id).all()
    member_groups = [Group.query.get(m.group_id) for m in memberships]
    all_groups = {g.id: g.to_dict() for g in created_groups + member_groups if g}
    return jsonify(list(all_groups.values())), 200

@groups_bp.route('', methods=['POST'])
@jwt_required()
def create_group():
    user_id = int(get_jwt_identity())
    data = request.get_json()
    
    group = Group(
        name=data['name'],
        description=data.get('description', ''),
        image_url=data.get('image_url'),
        created_by=user_id
    )
    
    db.session.add(group)
    db.session.commit()
    
    member = GroupMember(group_id=group.id, user_id=user_id, role='owner')
    db.session.add(member)
    db.session.commit()
    
    return jsonify(group.to_dict()), 201

@groups_bp.route('/<int:group_id>', methods=['GET'])
@jwt_required()
def get_group(group_id):
    group = Group.query.get_or_404(group_id)
    return jsonify(group.to_dict()), 200

@groups_bp.route('/<int:group_id>/upload-image', methods=['POST'])
@jwt_required()
def upload_group_image(group_id):
    user_id = int(get_jwt_identity())
    group = Group.query.get_or_404(group_id)
    
    if group.created_by != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    result = cloudinary.uploader.upload(image)
    
    group.image_url = result['secure_url']
    db.session.commit()
    
    return jsonify({'image_url': result['secure_url']}), 200

@groups_bp.route('/<int:group_id>/join', methods=['POST'])
@jwt_required()
def join_group(group_id):
    user_id = int(get_jwt_identity())
    group = Group.query.get_or_404(group_id)
    
    existing = GroupMember.query.filter_by(group_id=group_id, user_id=user_id).first()
    if existing:
        return jsonify({'message': 'Already a member'}), 200
    
    member = GroupMember(group_id=group_id, user_id=user_id, role='member')
    db.session.add(member)
    db.session.commit()
    
    return jsonify(member.to_dict()), 201

@groups_bp.route('/<int:group_id>/members', methods=['GET'])
@jwt_required()
def get_group_members(group_id):
    group = Group.query.get_or_404(group_id)
    members = GroupMember.query.filter_by(group_id=group_id).all()
    return jsonify([member.to_dict() for member in members]), 200

@groups_bp.route('/<int:group_id>/recipes', methods=['GET'])
@jwt_required()
def get_group_recipes(group_id):
    group = Group.query.get_or_404(group_id)
    recipes = Recipe.query.filter_by(group_id=group_id).all()
    return jsonify([recipe.to_dict(include_stats=True) for recipe in recipes]), 200

@groups_bp.route('/<int:group_id>/invite', methods=['POST'])
@jwt_required()
def invite_to_group(group_id):
    user_id = int(get_jwt_identity())
    group = Group.query.get_or_404(group_id)
    data = request.get_json()
    
    member = GroupMember.query.filter_by(group_id=group_id, user_id=user_id).first()
    if not member and group.created_by != user_id:
        return jsonify({'error': 'Only members can invite'}), 403
    
    invitation = GroupInvitation(
        group_id=group_id,
        inviter_id=user_id,
        invitee_email=data['email']
    )
    
    db.session.add(invitation)
    db.session.commit()
    
    return jsonify(invitation.to_dict()), 201

@groups_bp.route('/invitations', methods=['GET'])
@jwt_required()
def get_my_invitations():
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    
    invitations = GroupInvitation.query.filter_by(
        invitee_email=user.email,
        status='pending'
    ).all()
    
    return jsonify([inv.to_dict() for inv in invitations]), 200

@groups_bp.route('/invitations/<int:invitation_id>/accept', methods=['POST'])
@jwt_required()
def accept_invitation(invitation_id):
    user_id = int(get_jwt_identity())
    invitation = GroupInvitation.query.get_or_404(invitation_id)
    
    member = GroupMember(group_id=invitation.group_id, user_id=user_id, role='member')
    db.session.add(member)
    
    invitation.status = 'accepted'
    db.session.commit()
    
    return jsonify({'message': 'Invitation accepted'}), 200

@groups_bp.route('/invitations/<int:invitation_id>/decline', methods=['POST'])
@jwt_required()
def decline_invitation(invitation_id):
    invitation = GroupInvitation.query.get_or_404(invitation_id)
    invitation.status = 'declined'
    db.session.commit()
    return jsonify({'message': 'Invitation declined'}), 200
