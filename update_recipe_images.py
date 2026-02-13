from app import app
from database import db
from models import Recipe

def update_recipe_images():
    with app.app_context():
        updates = {
            'Nihari': 'https://i.pinimg.com/736x/f2/22/5e/f2225ef60cbdb43d8ca31c89fdcc4cc3.jpg',
            'Borscht': 'https://i.pinimg.com/1200x/65/eb/34/65eb34890385b0dbe727ec4f53cb7198.jpg',
            'Empanadas': 'https://i.pinimg.com/736x/be/45/f9/be45f96124c7622f31df40c54bb10d62.jpg',
            'Koshari': 'https://i.pinimg.com/1200x/75/b5/ab/75b5ab030e25cbfb222c480503143a60.jpg',
            'Feijoada': 'https://i.pinimg.com/1200x/c8/11/08/c81108e5203384e5bc805b72a90a056d.jpg'
        }
        
        for title, image_url in updates.items():
            recipe = Recipe.query.filter_by(title=title).first()
            if recipe:
                recipe.image_url = image_url
                print(f"Updated image for: {title}")
            else:
                print(f"Recipe not found: {title}")
        
        db.session.commit()
        print("\nSuccessfully updated all recipe images!")

if __name__ == '__main__':
    update_recipe_images()
