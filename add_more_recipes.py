from app import app
from database import db
from models import User, Recipe
from werkzeug.security import generate_password_hash

def add_more_recipes():
    with app.app_context():
        # Get or create additional users from different countries
        additional_users_data = [
            {'username': 'YukiTanaka', 'email': 'yuki@reciperoom.com', 'country': 'Japan'},
            {'username': 'LucasDaSilva', 'email': 'lucas@reciperoom.com', 'country': 'Brazil'},
            {'username': 'PierreDubois', 'email': 'pierre@reciperoom.com', 'country': 'France'},
            {'username': 'MeiLing', 'email': 'meiling@reciperoom.com', 'country': 'China'},
            {'username': 'FatimaHassan', 'email': 'fatimaeg@reciperoom.com', 'country': 'Egypt'},
            {'username': 'RajeshKumar', 'email': 'rajesh@reciperoom.com', 'country': 'India'},
            {'username': 'SofiaGarcia', 'email': 'sofia@reciperoom.com', 'country': 'Spain'},
            {'username': 'AhmedAli', 'email': 'ahmed@reciperoom.com', 'country': 'Turkey'},
            {'username': 'NguyenTran', 'email': 'nguyen@reciperoom.com', 'country': 'Vietnam'},
            {'username': 'OliviaSmith', 'email': 'olivia@reciperoom.com', 'country': 'Australia'},
            {'username': 'KwameAsante', 'email': 'kwame@reciperoom.com', 'country': 'Ghana'},
            {'username': 'IngeSchmidt', 'email': 'inge@reciperoom.com', 'country': 'Germany'},
            {'username': 'MariaGonzalez', 'email': 'maria@reciperoom.com', 'country': 'Argentina'},
            {'username': 'KimMinJi', 'email': 'minji@reciperoom.com', 'country': 'Korea'},
        ]
        
        users = {}
        
        # Get existing users
        existing_users = User.query.all()
        for user in existing_users:
            # Map users to their countries based on recipes they've created
            user_recipes = Recipe.query.filter_by(user_id=user.id).first()
            if user_recipes:
                users[user_recipes.country] = user
        
        # Create new users if they don't exist
        for user_data in additional_users_data:
            if user_data['country'] not in users:
                existing_user = User.query.filter_by(email=user_data['email']).first()
                if not existing_user:
                    user = User(
                        username=user_data['username'],
                        email=user_data['email'],
                        password_hash=generate_password_hash('password123')
                    )
                    db.session.add(user)
                    db.session.commit()
                    users[user_data['country']] = user
                    print(f"Created user: {user.username} from {user_data['country']}")
                else:
                    users[user_data['country']] = existing_user
        
        # Add many more diverse recipes
        new_recipes = [
            # More KENYAN recipes
            {
                'title': 'Mandazi (East African Donuts)',
                'description': 'Sweet, fluffy fried bread popular across East Africa. Perfect for breakfast or as a snack with tea.',
                'ingredients': '''3 cups all-purpose flour
1/2 cup sugar
1 teaspoon instant yeast
1/2 teaspoon cardamom powder
1/4 teaspoon salt
1 egg
1/2 cup coconut milk
1/4 cup warm water
Oil for deep frying''',
                'instructions': '''1. In a large bowl, mix flour, sugar, yeast, cardamom, and salt
2. In another bowl, whisk together egg, coconut milk, and warm water
3. Pour wet ingredients into dry and mix to form a soft dough
4. Knead for 8-10 minutes until smooth and elastic
5. Cover with a damp cloth and let rise for 1 hour until doubled
6. Roll out dough to 1/2 inch thickness on a floured surface
7. Cut into triangles or squares
8. Heat oil in a deep pan to 350°F
9. Fry mandazi in batches, turning once, until golden brown on both sides (2-3 minutes per side)
10. Drain on paper towels and serve warm with chai''',
                'prep_time': 20,
                'cook_time': 15,
                'servings': 12,
                'country': 'Kenya',
                'image_url': 'https://images.unsplash.com/photo-1586444248902-2f64eddc13df?w=600',
                'user_id': users['Kenya'].id
            },
            # ETHIOPIAN recipes
            {
                'title': 'Doro Wat (Ethiopian Chicken Stew)',
                'description': 'Rich, spicy chicken stew considered Ethiopia\'s national dish. Traditionally served on injera with hard-boiled eggs.',
                'ingredients': '''1 whole chicken, cut into pieces
4 large onions, finely chopped
4 tablespoons berbere spice
1/4 cup niter kibbeh (Ethiopian spiced butter)
6 cloves garlic, minced
2 inches ginger, grated
2 tablespoons tomato paste
4 hard-boiled eggs
1 cup chicken stock
Salt to taste
Juice of 1 lemon''',
                'instructions': '''1. In a large pot, dry-sauté the onions over medium heat until soft (no oil needed, about 15 minutes)
2. Add niter kibbeh and berbere spice, stir well for 2 minutes
3. Add garlic and ginger, cook for 2 minutes
4. Stir in tomato paste and chicken stock
5. Add chicken pieces, coating them well with the sauce
6. Bring to a boil, then reduce heat and simmer covered for 45 minutes
7. Prick the boiled eggs with a fork and add to the stew
8. Continue simmering for another 15 minutes
9. Add lemon juice and adjust seasoning
10. Serve hot over injera with the eggs nestled in the stew''',
                'prep_time': 30,
                'cook_time': 75,
                'servings': 6,
                'country': 'Ethiopia',
                'image_url': 'https://images.unsplash.com/photo-1589621316382-008455b857cd?w=600',
                'user_id': users['Ethiopia'].id
            },
            # NIGERIAN recipes
            {
                'title': 'Egusi Soup',
                'description': 'Hearty Nigerian soup made with ground melon seeds, leafy greens, and meat. A beloved comfort food.',
                'ingredients': '''2 cups ground egusi (melon seeds)
500g beef or goat meat
200g dried fish
2 cups chopped spinach or bitter leaf
1/2 cup palm oil
2 onions, chopped
3 tomatoes, blended
2 tablespoons ground crayfish
3 scotch bonnet peppers
2 stock cubes
Salt to taste''',
                'instructions': '''1. Season and cook meat with onions until tender (45 minutes)
2. Remove meat, save the stock
3. Heat palm oil in a pot, add remaining onions
4. Add blended tomatoes and fry for 10 minutes
5. Mix egusi with some stock to form a paste
6. Add egusi paste to the pot, stirring continuously
7. Pour in remaining stock gradually, stirring to prevent lumps
8. Add crayfish, peppers, and stock cubes
9. Simmer for 20 minutes, stirring occasionally
10. Add meat, dried fish, and greens
11. Cook for 5 more minutes until greens wilt
12. Serve with fufu, pounded yam, or eba''',
                'prep_time': 25,
                'cook_time': 80,
                'servings': 6,
                'country': 'Nigeria',
                'image_url': 'https://images.unsplash.com/photo-1604329758481-1f6e9be39a2e?w=600',
                'user_id': users['Nigeria'].id
            },
            # MOROCCAN recipes
            {
                'title': 'Chicken Bastilla (Moroccan Pie)',
                'description': 'Sweet and savory pie with layers of flaky pastry, spiced chicken, and almonds dusted with cinnamon sugar.',
                'ingredients': '''1 whole chicken
10 sheets phyllo dough
2 onions, grated
1 cup almonds, toasted and chopped
4 eggs
1/2 cup butter, melted
1/4 cup fresh parsley, chopped
1/4 cup fresh cilantro, chopped
2 teaspoons cinnamon
1 teaspoon ginger
1/2 teaspoon turmeric
1/4 cup powdered sugar
Pinch of saffron
Salt and pepper''',
                'instructions': '''1. Cook chicken with onions, spices, and saffron until tender (1 hour)
2. Shred chicken, discard bones
3. Reduce cooking liquid to 1 cup, beat in eggs and cook until scrambled
4. Toast almonds, mix with 1 tsp cinnamon and 2 tbsp powdered sugar
5. Preheat oven to 375°F
6. Brush a round baking dish with butter
7. Layer 5 phyllo sheets, brushing each with butter
8. Spread chicken mixture, then egg mixture
9. Add almond mixture in the center
10. Top with remaining phyllo sheets, tucking edges
11. Brush top generously with butter
12. Bake for 25-30 minutes until golden
13. Dust with cinnamon and powdered sugar
14. Cut into wedges and serve warm''',
                'prep_time': 40,
                'cook_time': 90,
                'servings': 8,
                'country': 'Morocco',
                'image_url': 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600',
                'user_id': users['Morocco'].id
            },
            # SOUTH AFRICAN recipes
            {
                'title': 'Bunny Chow',
                'description': 'Iconic Durban street food: hollowed-out loaf of bread filled with curry. Perfect for eating on the go.',
                'ingredients': '''4 bread loaves (quarter loaves)
500g mutton or chicken, cubed
2 onions, chopped
3 tomatoes, chopped
2 potatoes, cubed
3 tablespoons curry powder
1 tablespoon garam masala
4 cloves garlic, minced
1 inch ginger, grated
2 green chilies, chopped
1/4 cup oil
Salt to taste
Fresh coriander''',
                'instructions': '''1. Heat oil, sauté onions until golden
2. Add garlic, ginger, chilies, cook for 2 minutes
3. Add curry powder and garam masala, toast for 1 minute
4. Add meat, brown on all sides
5. Add tomatoes, cook until soft
6. Add potatoes and enough water to cover
7. Simmer covered for 45 minutes until meat is tender
8. Sauce should be thick; reduce if needed
9. Hollow out the bread loaves, reserving the tops
10. Fill each bread with hot curry
11. Place the bread "lid" on top
12. Serve immediately with extra coriander''',
                'prep_time': 20,
                'cook_time': 60,
                'servings': 4,
                'country': 'South Africa',
                'image_url': 'https://images.unsplash.com/photo-1585937421612-70e008356d80?w=600',
                'user_id': users['South Africa'].id
            },
            # JAPANESE recipes
            {
                'title': 'Ramen Bowl',
                'description': 'Rich, umami-packed noodle soup with tender pork, soft-boiled egg, and fresh toppings.',
                'ingredients': '''4 packs fresh ramen noodles
500g pork belly, sliced
6 cups chicken stock
2 tablespoons miso paste
2 tablespoons soy sauce
1 tablespoon sesame oil
4 soft-boiled eggs
2 cups baby spinach
4 green onions, sliced
1 sheet nori, cut into strips
1 tablespoon ginger, grated
3 cloves garlic, minced
Chili oil for serving''',
                'instructions': '''1. Marinate pork belly with soy sauce and ginger for 30 minutes
2. Sear pork in a hot pan until crispy, set aside
3. In a large pot, sauté garlic until fragrant
4. Add chicken stock, bring to a boil
5. Whisk in miso paste until dissolved
6. Add sesame oil and soy sauce
7. Simmer broth for 20 minutes
8. Meanwhile, cook noodles according to package instructions
9. Blanch spinach in boiling water for 30 seconds
10. Divide noodles among bowls
11. Ladle hot broth over noodles
12. Top with pork slices, halved soft-boiled eggs, spinach
13. Garnish with green onions, nori, and a drizzle of chili oil''',
                'prep_time': 40,
                'cook_time': 30,
                'servings': 4,
                'country': 'Japan',
                'image_url': 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600',
                'user_id': users['Japan'].id
            },
            {
                'title': 'Sushi Rolls (Maki)',
                'description': 'Fresh, colorful sushi rolls with crisp vegetables and seasoned rice wrapped in nori.',
                'ingredients': '''3 cups sushi rice
4 sheets nori
1/4 cup rice vinegar
2 tablespoons sugar
1 teaspoon salt
1 cucumber, julienned
1 avocado, sliced
200g fresh tuna or salmon
Pickled ginger
Wasabi
Soy sauce
Sesame seeds''',
                'instructions': '''1. Cook sushi rice according to package instructions
2. Heat vinegar, sugar, and salt until dissolved
3. Mix vinegar mixture into warm rice, cool to room temperature
4. Place nori sheet shiny side down on bamboo mat
5. Spread thin layer of rice, leaving 1 inch at top
6. Arrange cucumber, avocado, and fish in a line across center
7. Using the mat, roll tightly from bottom, sealing with water
8. Sprinkle sesame seeds on top of roll
9. Cut into 8 pieces with a sharp, wet knife
10. Serve with soy sauce, wasabi, and pickled ginger''',
                'prep_time': 30,
                'cook_time': 20,
                'servings': 4,
                'country': 'Japan',
                'image_url': 'https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=600',
                'user_id': users['Japan'].id
            },
            # BRAZILIAN recipes
            {
                'title': 'Feijoada (Brazilian Black Bean Stew)',
                'description': 'Brazil\'s national dish: a rich and hearty black bean stew with various cuts of pork.',
                'ingredients': '''500g black beans, soaked overnight
300g pork ribs
200g smoked sausage, sliced
200g bacon, cubed
1 bay leaf
4 cloves garlic, minced
2 onions, chopped
2 tomatoes, diced
1 orange, cut in wedges
3 tablespoons olive oil
Salt and pepper
Fresh parsley
For serving: white rice, collard greens, orange slices, farofa''',
                'instructions': '''1. Drain soaked beans, place in large pot with fresh water
2. Add bay leaf, bring to boil, then simmer for 1 hour
3. In another pan, fry bacon until crispy
4. Add pork ribs and brown on all sides
5. Add onions and garlic, sauté until soft
6. Transfer meat mixture to beans
7. Add sausage, tomatoes, and more water if needed
8. Simmer uncovered for 1.5 hours, stirring occasionally
9. Beans should be creamy, some smashed to thicken the stew
10. Season with salt and pepper
11. Squeeze orange wedges into stew, add the peels
12. Simmer 10 more minutes
13. Serve over white rice with collard greens, orange slices, and farofa''',
                'prep_time': 30,
                'cook_time': 180,
                'servings': 8,
                'country': 'Brazil',
                'image_url': 'https://images.unsplash.com/photo-1555617766-4558a58b7f2e?w=600',
                'user_id': users['Brazil'].id
            },
            # FRENCH recipes
            {
                'title': 'Coq au Vin (Chicken in Red Wine)',
                'description': 'Classic French braised chicken dish with red wine, mushrooms, and pearl onions.',
                'ingredients': '''1 whole chicken, cut into 8 pieces
750ml red wine (Burgundy)
200g pearl onions, peeled
250g button mushrooms, halved
150g bacon lardons
2 carrots, chopped
2 cloves garlic, crushed
2 tablespoons tomato paste
2 tablespoons flour
3 tablespoons butter
2 bay leaves
4 sprigs fresh thyme
2 tablespoons cognac
Salt and pepper
Fresh parsley''',
                'instructions': '''1. Season chicken pieces with salt and pepper
2. In a large Dutch oven, render bacon until crispy
3. Brown chicken pieces in bacon fat, set aside
4. Sauté pearl onions and mushrooms, set aside
5. Add carrots and garlic, cook for 3 minutes
6. Sprinkle flour over vegetables, stir well
7. Pour in cognac and carefully flambe
8. Add wine, tomato paste, bay leaves, and thyme
9. Return chicken to pot, ensuring it's submerged
10. Bring to simmer, cover, and braise for 1 hour
11. Add pearl onions and mushrooms, cook 30 more minutes
12. Remove chicken, reduce sauce if needed
13. Whisk in butter for glossy finish
14. Return chicken to sauce, garnish with parsley
15. Serve with crusty bread or mashed potatoes''',
                'prep_time': 30,
                'cook_time': 90,
                'servings': 6,
                'country': 'France',
                'image_url': 'https://images.unsplash.com/photo-1610769158338-ded378dd3f4b?w=600',
                'user_id': users['France'].id
            },
            # CHINESE recipes
            {
                'title': 'Mapo Tofu',
                'description': 'Spicy Sichuan dish featuring silky tofu in a fiery, numbing sauce with ground pork.',
                'ingredients': '''500g soft tofu, cubed
250g ground pork
3 tablespoons doubanjiang (chili bean paste)
2 tablespoons fermented black beans
4 cloves garlic, minced
1 inch ginger, minced
2 green onions, chopped
1 cup chicken stock
2 tablespoons soy sauce
1 tablespoon Shaoxing wine
1 teaspoon Sichuan peppercorns, ground
2 tablespoons cornstarch mixed with water
2 tablespoons vegetable oil
Chili oil to taste''',
                'instructions': '''1. Heat wok over high heat, add oil
2. Brown ground pork, breaking it apart
3. Add garlic, ginger, black beans, stir-fry for 30 seconds
4. Add doubanjiang and cook for 2 minutes
5. Pour in stock, soy sauce, and wine
6. Bring to a boil, add tofu cubes gently
7. Reduce heat and simmer for 5 minutes
8. Add Sichuan peppercorn powder
9. Thicken sauce with cornstarch slurry
10. Drizzle with chili oil
11. Garnish with green onions
12. Serve over steamed white rice''',
                'prep_time': 15,
                'cook_time': 15,
                'servings': 4,
                'country': 'China',
                'image_url': 'https://images.unsplash.com/photo-1633699944763-8e1e3f3b78a6?w=600',
                'user_id': users['China'].id
            },
            {
                'title': 'Peking Duck',
                'description': 'Crispy-skinned duck with thin pancakes, cucumber, and hoisin sauce. A Beijing specialty.',
                'ingredients': '''1 whole duck (about 2kg)
2 tablespoons maltose syrup
2 tablespoons Shaoxing wine
1 teaspoon five-spice powder
1 cucumber, julienned
6 green onions, cut into strips
Chinese pancakes
Hoisin sauce
Salt''',
                'instructions': '''1. Clean duck inside and out, pat completely dry
2. Blanch duck in boiling water for 1 minute
3. Hang duck to dry in a cool, airy place for 4-6 hours
4. Mix maltose with boiling water, brush over entire duck
5. Let air-dry overnight in refrigerator
6. Preheat oven to 350°F
7. Rub duck cavity with salt and five-spice powder
8. Place duck on roasting rack
9. Roast for 30 minutes
10. Increase heat to 450°F, roast 20 more minutes for crispy skin
11. Let rest 10 minutes
12. Carve skin in crispy pieces, slice meat separately
13. Serve with warm pancakes, cucumber, green onions, and hoisin sauce
14. To eat: spread hoisin on pancake, add duck, vegetables, roll up''',
                'prep_time': 30,
                'cook_time': 50,
                'servings': 6,
                'country': 'China',
                'image_url': 'https://images.unsplash.com/photo-1588347818036-b6d906f7e5e5?w=600',
                'user_id': users['China'].id
            },
            # EGYPTIAN recipes
            {
                'title': 'Koshari',
                'description': 'Egypt\'s beloved street food combining rice, lentils, pasta, and crispy onions in tangy tomato sauce.',
                'ingredients': '''1 cup brown lentils
1 cup rice
1 cup small pasta (elbow or ditalini)
1 cup vermicelli noodles, broken
3 onions, thinly sliced
4 cloves garlic, minced
400g canned tomatoes
2 tablespoons tomato paste
1 tablespoon vinegar
1 teaspoon cumin
1/2 teaspoon cayenne pepper
Oil for frying
Salt and pepper''',
                'instructions': '''1. Cook lentils in salted water until tender (25 minutes), drain
2. Cook rice in 2 cups water until fluffy
3. Cook pasta according to package instructions
4. Fry vermicelli in oil until golden, drain
5. Heat oil, fry onion rings until deep brown and crispy, drain
6. For sauce: sauté garlic, add tomatoes, paste, cumin, cayenne
7. Simmer sauce for 15 minutes, add vinegar
8. In bowls, layer rice, lentils, pasta, and vermicelli
9. Top with generous amount of crispy onions
10. Pour hot tomato sauce over everything
11. Mix well before eating for best flavor combination''',
                'prep_time': 20,
                'cook_time': 45,
                'servings': 6,
                'country': 'Egypt',
                'image_url': 'https://images.unsplash.com/photo-1605755962947-e73e24fc3553?w=600',
                'user_id': users['Egypt'].id
            },
            # More INDIAN recipes
            {
                'title': 'Butter Chicken (Murgh Makhani)',
                'description': 'Creamy, rich tomato-based curry with tender chicken pieces. A restaurant favorite.',
                'ingredients': '''800g chicken thighs, cubed
1 cup plain yogurt
2 tablespoons ginger-garlic paste
1 tablespoon garam masala
1 teaspoon turmeric
1 teaspoon chili powder
400g crushed tomatoes
1 cup heavy cream
3 tablespoons butter
1 onion, finely chopped
2 tablespoons kasuri methi (dried fenugreek)
1 tablespoon honey
Salt to taste
Fresh cilantro''',
                'instructions': '''1. Marinate chicken with yogurt, half the garam masala, turmeric, chili powder for 2 hours
2. Grill or broil chicken pieces until slightly charred, set aside
3. In a large pan, melt butter and sauté onions until soft
4. Add ginger-garlic paste, cook for 2 minutes
5. Add crushed tomatoes, simmer for 15 minutes
6. Blend sauce until smooth, return to pan
7. Add remaining garam masala, kasuri methi, honey
8. Stir in cream and grilled chicken
9. Simmer for 10 minutes
10. Adjust seasoning with salt
11. Garnish with cilantro
12. Serve with naan or basmati rice''',
                'prep_time': 20,
                'cook_time': 35,
                'servings': 6,
                'country': 'India',
                'image_url': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=600',
                'user_id': users['India'].id
            },
            # SPANISH recipes
            {
                'title': 'Paella Valenciana',
                'description': 'Spain\'s iconic rice dish with chicken, rabbit, and vegetables. Traditionally cooked outdoors.',
                'ingredients': '''2 cups Bomba rice
1 chicken, cut into pieces
300g rabbit, cut into pieces
200g green beans, trimmed
1 cup lima beans
2 tomatoes, grated
1 teaspoon sweet paprika
Pinch of saffron
6 cups chicken stock
1/2 cup olive oil
1 sprig rosemary
Salt to taste''',
                'instructions': '''1. Heat olive oil in a paella pan over medium-high heat
2. Brown chicken and rabbit pieces, season with salt
3. Add green beans and lima beans, sauté for 5 minutes
4. Stir in grated tomatoes and paprika
5. Add rice, stir to coat with oil
6. Pour in hot stock and saffron
7. Add rosemary sprig
8. Bring to a boil, then reduce to simmer
9. Do not stir from this point
10. Cook for 18-20 minutes until rice absorbs liquid
11. Increase heat for last 2 minutes for crispy bottom (socarrat)
12. Remove from heat, cover with cloth for 5 minutes
13. Serve directly from the pan with lemon wedges''',
                'prep_time': 25,
                'cook_time': 45,
                'servings': 6,
                'country': 'Spain',
                'image_url': 'https://images.unsplash.com/photo-1534080564583-6be75777b70a?w=600',
                'user_id': users['Spain'].id
            },
            # TURKISH recipes
            {
                'title': 'Manti (Turkish Dumplings)',
                'description': 'Tiny handmade dumplings filled with spiced meat, served with yogurt and butter sauce.',
                'ingredients': '''For dough: 3 cups flour, 1 egg, 1 tsp salt, 1 cup water
For filling: 300g ground lamb, 1 onion grated, 2 tsp paprika, salt, pepper
For serving: 2 cups yogurt, 4 cloves garlic minced, 4 tbsp butter, 1 tsp red pepper flakes, dried mint''',
                'instructions': '''1. Make dough: mix flour, egg, salt, and water; knead until smooth, rest 30 minutes
2. For filling: mix lamb, onion, paprika, salt, and pepper
3. Roll dough very thin, cut into 2-inch squares
4. Place small amount of filling in center of each square
5. Fold corners to center, pinching to seal
6. Bring large pot of salted water to boil
7. Cook manti in batches until they float (8-10 minutes)
8. Mix yogurt with minced garlic
9. Brown butter with red pepper flakes
10. Place cooked manti in serving bowl
11. Top with yogurt sauce
12. Drizzle with spiced butter
13. Sprinkle with dried mint and extra paprika''',
                'prep_time': 60,
                'cook_time': 20,
                'servings': 4,
                'country': 'Turkey',
                'image_url': 'https://images.unsplash.com/photo-1534080564583-6be75777b70a?w=600',
                'user_id': users['Turkey'].id
            },
            # VIETNAMESE recipes
            {
                'title': 'Banh Mi Sandwich',
                'description': 'Vietnamese baguette sandwich with savory-sweet pork, pickled vegetables, and fresh herbs.',
                'ingredients': '''4 Vietnamese baguettes
400g pork shoulder, thinly sliced
2 tablespoons fish sauce
2 tablespoons soy sauce
2 tablespoons honey
4 cloves garlic, minced
1 daikon radish, julienned
2 carrots, julienned
1/4 cup rice vinegar
1 tablespoon sugar
Mayonnaise
Fresh cilantro
Cucumber slices
Jalapeños, sliced
Paté (optional)''',
                'instructions': '''1. Marinate pork with fish sauce, soy sauce, honey, and garlic for 2 hours
2. Make pickles: combine daikon, carrots with vinegar, sugar, and salt; refrigerate 30 minutes
3. Grill or pan-fry pork until caramelized and cooked through
4. Toast baguettes until crispy outside, soft inside
5. Spread mayonnaise on both sides of bread
6. Optional: spread paté on bottom half
7. Layer with grilled pork
8. Add pickled vegetables
9. Top with cucumber slices
10. Add fresh cilantro and jalapeños
11. Close sandwich and serve immediately''',
                'prep_time': 30,
                'cook_time': 15,
                'servings': 4,
                'country': 'Vietnam',
                'image_url': 'https://images.unsplash.com/photo-1591814264808-e1c4a2d95882?w=600',
                'user_id': users['Vietnam'].id
            },
            # AUSTRALIAN recipes
            {
                'title': 'Meat Pie',
                'description': 'Classic Australian hand pie filled with savory beef and gravy. Perfect for footy matches.',
                'ingredients': '''500g ground beef
1 onion, finely chopped
2 cloves garlic, minced
2 tablespoons flour
1 cup beef stock
2 tablespoons Worcestershire sauce
1 tablespoon tomato paste
2 sheets puff pastry
1 egg, beaten
Salt and pepper
Tomato ketchup for serving''',
                'instructions': '''1. Brown beef and onion in a pan over medium heat
2. Add garlic, cook for 1 minute
3. Sprinkle flour over meat, stir well
4. Add stock, Worcestershire sauce, and tomato paste
5. Simmer for 20 minutes until thick, season with salt and pepper
6. Let filling cool completely
7. Preheat oven to 400°F
8. Cut pastry circles to fit pie tins
9. Line tins with pastry, trim edges
10. Fill with cooled beef mixture
11. Top with pastry lids, seal edges with fork
12. Brush tops with beaten egg
13. Cut small steam vents in top
14. Bake for 25-30 minutes until golden brown
15. Serve hot with tomato ketchup''',
                'prep_time': 30,
                'cook_time': 50,
                'servings': 6,
                'country': 'Australia',
                'image_url': 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600',
                'user_id': users['Australia'].id
            },
            # GHANAIAN recipes
            {
                'title': 'Jollof Rice (Ghanaian Style)',
                'description': 'West Africa\'s most celebrated rice dish with tomatoes, peppers, and aromatic spices.',
                'ingredients': '''3 cups long grain rice
400g can tomatoes
3 red bell peppers
2 onions
4 cloves garlic
2 inch ginger
3 tablespoons tomato paste
1/4 cup vegetable oil
2 bay leaves
1 teaspoon thyme
1 teaspoon curry powder
2 stock cubes
3 cups chicken stock
2 scotch bonnet peppers
Salt to taste''',
                'instructions': '''1. Blend tomatoes, bell peppers, onions, garlic, and ginger until smooth
2. Heat oil in a large pot over medium heat
3. Fry tomato paste for 3 minutes to remove raw taste
4. Pour in blended mixture, fry for 20 minutes until oil rises
5. Add thyme, curry powder, stock cubes, and bay leaves
6. Add scotch bonnet peppers (whole for less heat)
7. Pour in chicken stock and bring to boil
8. Wash rice and add to pot
9. Stir once, reduce heat to low
10. Cover tightly and cook for 30 minutes without stirring
11. Rice should absorb all liquid and be fluffy
12. Fluff with fork and serve with fried plantains and grilled chicken''',
                'prep_time': 20,
                'cook_time': 60,
                'servings': 8,
                'country': 'Ghana',
                'image_url': 'https://images.unsplash.com/photo-1604329760661-e71dc83f8f26?w=600',
                'user_id': users['Ghana'].id
            },
            # GERMAN recipes
            {
                'title': 'Sauerbraten',
                'description': 'Traditional German pot roast marinated in wine and vinegar with a sweet-sour gravy.',
                'ingredients': '''2kg beef roast
2 cups red wine
1 cup red wine vinegar
2 onions, sliced
2 carrots, chopped
2 bay leaves
6 cloves
6 juniper berries
10 black peppercorns
2 tablespoons sugar
3 tablespoons flour
1/2 cup crushed gingersnap cookies
2 tablespoons butter
Salt''',
                'instructions': '''1. Combine wine, vinegar, onions, carrots, spices in a bowl
2. Add beef, ensure it\'s submerged
3. Marinate in refrigerator for 3-5 days, turning daily
4. Remove beef, pat dry, season with salt
5. Strain marinade, reserve liquid and vegetables
6. Brown beef in butter on all sides
7. Add strained vegetables, cook until soft
8. Pour in marinade, bring to boil
9. Reduce heat, cover, simmer for 2.5-3 hours until tender
10. Remove beef, keep warm
11. Strain sauce, return to pan
12. Add sugar and crushed gingersnaps, simmer until thick
13. Slice beef, serve with gravy
14. Traditional sides: red cabbage and potato dumplings''',
                'prep_time': 30,
                'cook_time': 180,
                'servings': 8,
                'country': 'Germany',
                'image_url': 'https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?w=600',
                'user_id': users['Germany'].id
            },
            # ARGENTINIAN recipes
            {
                'title': 'Empanadas',
                'description': 'Savory pastries filled with spiced beef, olives, and eggs. Argentina\'s favorite snack.',
                'ingredients': '''For dough: 4 cups flour, 1/2 cup butter, 1 cup warm water, 1 tsp salt
For filling: 500g ground beef, 2 onions chopped, 2 hard-boiled eggs chopped, 1/2 cup green olives, 2 tsp cumin, 1 tsp paprika, salt, pepper
1 egg for brushing''',
                'instructions': '''1. Make dough: mix flour and salt, cut in butter, add water; knead until smooth, rest 1 hour
2. Cook onions until soft, add beef and brown
3. Season with cumin, paprika, salt, and pepper
4. Remove from heat, stir in chopped eggs and olives
5. Let filling cool completely
6. Roll dough thin, cut into 5-inch circles
7. Place spoonful of filling on each circle
8. Fold in half, seal edges with fork
9. Brush with beaten egg
10. Bake at 400°F for 20-25 minutes until golden
11. Or deep fry until crispy and golden
12. Serve hot or room temperature with chimichurri''',
                'prep_time': 90,
                'cook_time': 25,
                'servings': 12,
                'country': 'Argentina',
                'image_url': 'https://images.unsplash.com/photo-1599667605801-5a8f3e8347e6?w=600',
                'user_id': users['Argentina'].id
            },
            # KOREAN recipes
            {
                'title': 'Bibimbap',
                'description': 'Colorful rice bowl topped with seasoned vegetables, egg, and gochujang sauce.',
                'ingredients': '''3 cups cooked rice
200g beef, thinly sliced
1 zucchini, julienned
1 carrot, julienned
200g bean sprouts
200g spinach
4 eggs
4 tablespoons gochujang
2 tablespoons sesame oil
2 tablespoons soy sauce
2 cloves garlic, minced
Sesame seeds
Cooking oil''',
                'instructions': '''1. Marinate beef with soy sauce, garlic, sesame oil for 30 minutes
2. Blanch spinach and bean sprouts separately, squeeze dry
3. Sauté zucchini and carrot separately with a little oil
4. Season each vegetable with sesame oil and salt
5. Cook beef until browned
6. Fry eggs sunny-side up
7. Divide rice among bowls
8. Arrange vegetables and beef in sections on top of rice
9. Place fried egg in center
10. Mix gochujang with sesame oil and a little water
11. Drizzle sauce over bowls
12. Sprinkle with sesame seeds
13. Mix everything together before eating''',
                'prep_time': 40,
                'cook_time': 20,
                'servings': 4,
                'country': 'Korea',
                'image_url': 'https://images.unsplash.com/photo-1553163147-622ab57be1c7?w=600',
                'user_id': users['Korea'].id
            },
        ]
        
        # Add all new recipes
        for recipe_data in new_recipes:
            recipe = Recipe(**recipe_data)
            db.session.add(recipe)
        
        db.session.commit()
        print(f"\n✅ Successfully added {len(new_recipes)} more recipes!")
        
        # Show distribution
        all_recipes = Recipe.query.all()
        countries_count = {}
        for recipe in all_recipes:
            countries_count[recipe.country] = countries_count.get(recipe.country, 0) + 1
        
        print("\n📊 Recipe distribution by country:")
        for country, count in sorted(countries_count.items()):
            print(f"  {country}: {count} recipes")
        print(f"\n🌍 Total recipes in database: {len(all_recipes)}")

if __name__ == '__main__':
    add_more_recipes()
