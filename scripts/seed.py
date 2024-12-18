from recipes.models import Recipe, Ingredient

def seed_data():
    recipes_data = [
        {
            "name": "Air Fryer Crispy Chilli Beef",
            "category": "Main Course",
            "difficulty": "Medium",
            "prep_time": "15 minutes",
            "cooking_time": "10 minutes",
            "base_servings": 4,
            "current_servings": 4,
            "ingredients": [
                {"base_quantity": 500, "unit": "g", "name": "beef steak, sliced into strips"},
                {"base_quantity": 3, "unit": "tbsp", "name": "cornflour"},
                {"base_quantity": 1, "unit": "tbsp", "name": "soy sauce"},
                {"base_quantity": 2, "unit": "tbsp", "name": "sweet chilli sauce"},
                {"base_quantity": 1, "unit": "tbsp", "name": "rice vinegar"},
                {"base_quantity": 1, "unit": "", "name": "ketchup"},
                {"base_quantity": 1, "unit": "", "name": "red chilli, finely sliced"},
                {"base_quantity": 2, "unit": "tbsp", "name": "vegetable oil"},
                {"base_quantity": 2, "unit": "", "name": "spring onions, finely sliced"},
            ],
            "pre_prep_instructions": "Slice the beef into thin strips and pat dry.",
            "instructions": """
            Place the beef strips in a bowl, add cornflour, and toss to coat evenly.
            Preheat the air fryer to 200°C.
            Lightly spray the air fryer basket with oil and add the beef strips in a single layer.
            Cook for 8-10 minutes, shaking halfway through until crispy.
            In a separate bowl, mix soy sauce, sweet chilli sauce, rice vinegar, ketchup, and red chilli.
            Heat the sauce mixture in a pan until it starts to thicken.
            Add the cooked beef to the pan and toss to coat in the sauce.
            Garnish with spring onions before serving.
            """,
            "notes": "Serve immediately with steamed rice or noodles for a delicious and crispy meal.",
        },
        {
            "name": "Achari Chicken Curry (Instant Pot Version)",
            "category": "Main Course",
            "difficulty": "Medium",
            "prep_time": "20 minutes",
            "cooking_time": "20 minutes",
            "base_servings": 4,
            "current_servings": 4,
            "ingredients": [
                {"base_quantity": 3, "unit": "tbsp", "name": "oil of choice"},
                {"base_quantity": 1, "unit": "tsp", "name": "cumin seeds"},
                {"base_quantity": 1, "unit": "", "name": "bay leaf"},
                {"base_quantity": 1, "unit": "", "name": "onion, diced"},
                {"base_quantity": 1, "unit": "tsp", "name": "minced garlic"},
                {"base_quantity": 1, "unit": "tsp", "name": "minced ginger"},
                {"base_quantity": 1, "unit": "tsp", "name": "coriander powder"},
                {"base_quantity": 1, "unit": "tsp", "name": "fennel seeds"},
                {"base_quantity": 1, "unit": "tsp", "name": "paprika"},
                {"base_quantity": 1, "unit": "tsp", "name": "salt"},
                {"base_quantity": 1, "unit": "tsp", "name": "turmeric"},
                {"base_quantity": 0.5, "unit": "tsp", "name": "amchur (dried mango powder)"},
                {"base_quantity": 0.5, "unit": "tsp", "name": "fenugreek (methi) seeds"},
                {"base_quantity": 0.5, "unit": "tsp", "name": "garam masala"},
                {"base_quantity": 0.5, "unit": "tsp", "name": "kalonji (nigella seeds)"},
                {"base_quantity": 0.25, "unit": "tsp", "name": "black pepper"},
                {"base_quantity": 0.25, "unit": "tsp", "name": "cayenne"},
                {"base_quantity": 2, "unit": "lbs", "name": "skinless and boneless chicken thighs, cut into bite-sized pieces"},
                {"base_quantity": 1, "unit": "cup", "name": "fresh tomato puree"},
            ],
            "pre_prep_instructions": "Chop onions and garlic.",
            "instructions": """
            Press the sauté button on the Instant Pot, add the oil, and allow it to heat up for a minute.
            Once the oil is hot, add the cumin seeds and bay leaf.
            When the cumin seeds brown, add the diced onion and stir-fry for 6-7 minutes, or until the onions begin to brown.
            Add the minced garlic and ginger, stir, then add all the spices. Mix well.
            Add the chicken pieces and stir-fry for 5-6 minutes, or until the chicken is mostly cooked.
            Add the fresh tomato puree and mix well.
            Secure the lid, close the pressure valve, and cook for 5 minutes at high pressure.
            Naturally release pressure.
            Garnish with cilantro and serve.
            """,
            "notes": "A flavorful and tangy chicken curry, perfect for pairing with naan or rice.",
        },
    ]

    for recipe_data in recipes_data:
        recipe = Recipe.objects.create(
            name=recipe_data["name"],
            category=recipe_data["category"],
            difficulty=recipe_data["difficulty"],
            prep_time=recipe_data["prep_time"],
            cooking_time=recipe_data["cooking_time"],
            base_servings=recipe_data["base_servings"],
            current_servings=recipe_data["current_servings"],
            pre_prep_instructions=recipe_data["pre_prep_instructions"],
            instructions=recipe_data["instructions"],
            notes=recipe_data["notes"]
        )

        for ingredient_data in recipe_data["ingredients"]:
            ingredient = Ingredient.objects.create(
                name=ingredient_data["name"],
                unit=ingredient_data["unit"],
                base_quantity=ingredient_data["base_quantity"]
            )
            recipe.ingredients.add(ingredient)
        
        print(f"Recipe '{recipe.name}' and it's ingredients have been successfully seeded!")
      