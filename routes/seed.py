from flask import Blueprint, jsonify
from database import db
from models import User, Recipe
from werkzeug.security import generate_password_hash

seed_bp = Blueprint('seed', __name__)

@seed_bp.route('/seed-recipes', methods=['POST'])
def seed_recipes():
    try:
        new_users = [
            {'username': 'YukiTanaka', 'email': 'yuki@flavorhub.com', 'country': 'Japan'},
            {'username': 'PierreDubois', 'email': 'pierre@flavorhub.com', 'country': 'France'},
            {'username': 'MariaSantos', 'email': 'maria@flavorhub.com', 'country': 'Brazil'},
            {'username': 'AhmedKhalil', 'email': 'ahmed@flavorhub.com', 'country': 'Egypt'},
            {'username': 'LiWei', 'email': 'liwei@flavorhub.com', 'country': 'China'},
            {'username': 'OlgaPetrova', 'email': 'olga@flavorhub.com', 'country': 'Russia'},
            {'username': 'DiegoGarcia', 'email': 'diego@flavorhub.com', 'country': 'Spain'},
            {'username': 'KwameAsante', 'email': 'kwame@flavorhub.com', 'country': 'Ghana'},
            {'username': 'SophiaKowalski', 'email': 'sophia@flavorhub.com', 'country': 'Poland'},
            {'username': 'IsabellaRomano', 'email': 'isabella@flavorhub.com', 'country': 'Argentina'},
            {'username': 'HassanMohamed', 'email': 'hassan@flavorhub.com', 'country': 'Somalia'},
            {'username': 'NurhayatiSukarno', 'email': 'nurhayati@flavorhub.com', 'country': 'Indonesia'},
            {'username': 'KofiMensah', 'email': 'kofi@flavorhub.com', 'country': 'Ivory Coast'},
            {'username': 'AnastasiaVolkov', 'email': 'anastasia@flavorhub.com', 'country': 'Ukraine'},
            {'username': 'RajeshPatel', 'email': 'rajesh@flavorhub.com', 'country': 'Pakistan'},
        ]
        
        users = {}
        for user_data in new_users:
            existing = User.query.filter_by(username=user_data['username']).first()
            if not existing:
                user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password_hash=generate_password_hash('password123')
                )
                db.session.add(user)
                db.session.flush()
                users[user_data['country']] = user
            else:
                users[user_data['country']] = existing
        
        new_recipes = [
            {'title': 'Sushi Rolls', 'description': 'Fresh Japanese sushi with vinegared rice, nori, and fresh fish', 'ingredients': '2 cups sushi rice\n3 cups water\n1/4 cup rice vinegar\nNori sheets\nFresh salmon', 'instructions': '1. Cook sushi rice\n2. Mix vinegar\n3. Roll with nori', 'prep_time': 30, 'cook_time': 20, 'servings': 4, 'country': 'Japan', 'image_url': 'https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=600', 'user_id': users['Japan'].id},
            {'title': 'Coq au Vin', 'description': 'Classic French braised chicken in red wine', 'ingredients': '1 whole chicken\n750ml red wine\n200g bacon', 'instructions': '1. Brown bacon\n2. Brown chicken\n3. Add wine', 'prep_time': 20, 'cook_time': 65, 'servings': 4, 'country': 'France', 'image_url': 'https://images.unsplash.com/photo-1598103442097-8b74394b95c6?w=600', 'user_id': users['France'].id},
            {'title': 'Feijoada', 'description': 'Brazilian black bean stew with pork', 'ingredients': '500g black beans\n300g pork ribs\n200g bacon', 'instructions': '1. Soak beans\n2. Cook beans\n3. Add meats', 'prep_time': 720, 'cook_time': 150, 'servings': 8, 'country': 'Brazil', 'image_url': 'https://images.unsplash.com/photo-1623855244183-c5e8f29c6c4d?w=600', 'user_id': users['Brazil'].id},
            {'title': 'Koshari', 'description': 'Egyptian street food with rice, lentils, pasta', 'ingredients': '1 cup rice\n1 cup lentils\n1 cup pasta', 'instructions': '1. Cook rice\n2. Cook lentils\n3. Layer all', 'prep_time': 15, 'cook_time': 40, 'servings': 6, 'country': 'Egypt', 'image_url': 'https://images.unsplash.com/photo-1585937421612-70e008356f33?w=600', 'user_id': users['Egypt'].id},
            {'title': 'Kung Pao Chicken', 'description': 'Spicy Sichuan stir-fry with chicken and peanuts', 'ingredients': '500g chicken\n1/2 cup peanuts\n10 dried chilies', 'instructions': '1. Cube chicken\n2. Stir-fry\n3. Add sauce', 'prep_time': 20, 'cook_time': 10, 'servings': 4, 'country': 'China', 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600', 'user_id': users['China'].id},
            {'title': 'Beef Stroganoff', 'description': 'Russian comfort food with tender beef', 'ingredients': '600g beef\n300g mushrooms\n1 cup sour cream', 'instructions': '1. Brown beef\n2. Cook mushrooms\n3. Add cream', 'prep_time': 15, 'cook_time': 25, 'servings': 4, 'country': 'Russia', 'image_url': 'https://images.unsplash.com/photo-1600891964092-4316c288032e?w=600', 'user_id': users['Russia'].id},
            {'title': 'Paella Valenciana', 'description': 'Spanish rice dish with chicken and rabbit', 'ingredients': '2 cups rice\n500g chicken\n300g rabbit', 'instructions': '1. Brown meats\n2. Add rice\n3. Add stock', 'prep_time': 20, 'cook_time': 45, 'servings': 6, 'country': 'Spain', 'image_url': 'https://images.unsplash.com/photo-1534080564583-6be75777b70a?w=600', 'user_id': users['Spain'].id},
            {'title': 'Jollof Rice', 'description': 'Ghanaian rice dish', 'ingredients': '3 cups rice\n400g tomato paste', 'instructions': '1. Fry tomato paste\n2. Add rice\n3. Cook', 'prep_time': 30, 'cook_time': 55, 'servings': 6, 'country': 'Ghana', 'image_url': 'https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=600', 'user_id': users['Ghana'].id},
            {'title': 'Pierogi', 'description': 'Polish dumplings with potato', 'ingredients': '3 cups flour\n4 potatoes\n200g cheese', 'instructions': '1. Make dough\n2. Fill\n3. Boil', 'prep_time': 60, 'cook_time': 30, 'servings': 6, 'country': 'Poland', 'image_url': 'https://images.unsplash.com/photo-1626200419199-391ae4be7a41?w=600', 'user_id': users['Poland'].id},
            {'title': 'Empanadas', 'description': 'Argentine baked pastries with beef', 'ingredients': '500g beef\n2 onions\nEmpanada dough', 'instructions': '1. Cook beef\n2. Fill dough\n3. Bake', 'prep_time': 40, 'cook_time': 25, 'servings': 12, 'country': 'Argentina', 'image_url': 'https://images.unsplash.com/photo-1599974789516-e36e5d2f1a8d?w=600', 'user_id': users['Argentina'].id},
            {'title': 'Bariis Iskukaris', 'description': 'Somali spiced rice with lamb', 'ingredients': '2 cups rice\n500g lamb\n1/4 cup raisins', 'instructions': '1. Marinate lamb\n2. Cook rice\n3. Combine', 'prep_time': 30, 'cook_time': 50, 'servings': 6, 'country': 'Somalia', 'image_url': 'https://images.unsplash.com/photo-1596797038530-2c107229654b?w=600', 'user_id': users['Somalia'].id},
            {'title': 'Nasi Goreng', 'description': 'Indonesian fried rice', 'ingredients': '4 cups rice\n3 eggs\n200g chicken', 'instructions': '1. Fry paste\n2. Add rice\n3. Top with egg', 'prep_time': 20, 'cook_time': 15, 'servings': 4, 'country': 'Indonesia', 'image_url': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=600', 'user_id': users['Indonesia'].id},
            {'title': 'Kedjenou', 'description': 'Ivorian slow-cooked chicken stew', 'ingredients': '1 chicken\n3 tomatoes\n2 eggplants', 'instructions': '1. Layer ingredients\n2. Cook slowly\n3. Shake pot', 'prep_time': 20, 'cook_time': 90, 'servings': 4, 'country': 'Ivory Coast', 'image_url': 'https://images.unsplash.com/photo-1598103442097-8b74394b95c6?w=600', 'user_id': users['Ivory Coast'].id},
            {'title': 'Borscht', 'description': 'Ukrainian beet soup', 'ingredients': '4 beets\n2 potatoes\n400g cabbage', 'instructions': '1. Grate beets\n2. Simmer\n3. Add sour cream', 'prep_time': 20, 'cook_time': 45, 'servings': 6, 'country': 'Ukraine', 'image_url': 'https://images.unsplash.com/photo-1604908815453-e9d1b0a6e4f7?w=600', 'user_id': users['Ukraine'].id},
            {'title': 'Nihari', 'description': 'Pakistani slow-cooked beef stew', 'ingredients': '1kg beef shank\n2 onions\nNihari masala', 'instructions': '1. Brown onions\n2. Add beef\n3. Simmer 4 hours', 'prep_time': 20, 'cook_time': 240, 'servings': 6, 'country': 'Pakistan', 'image_url': 'https://images.unsplash.com/photo-1585937421612-70e008356f33?w=600', 'user_id': users['Pakistan'].id},
        ]
        
        for recipe_data in new_recipes:
            existing = Recipe.query.filter_by(title=recipe_data['title']).first()
            if not existing:
                recipe = Recipe(**recipe_data)
                db.session.add(recipe)
        
        db.session.commit()
        return jsonify({'message': 'Recipes seeded successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
