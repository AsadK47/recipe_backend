from recipes.models import Recipe, Ingredient

def seed_data():
  ingredient1 = Ingredient.objects.create(name="beef steak, sliced into strips", unit="g", base_quantity=500)
  ingredient2 = Ingredient.objects.create(name="cornflour", unit="tbsp", base_quantity=3)
  ingredient3 = Ingredient.objects.create(name="soy sauce", unit="tbsp", base_quantity=1)
  ingredient4 = Ingredient.objects.create(name="sweet chilli sauce", unit="tbsp", base_quantity=2)
  ingredient5 = Ingredient.objects.create(name="rice vinegar", unit="tbsp", base_quantity=1)
  ingredient6 = Ingredient.objects.create(name="ketchup", unit="", base_quantity=1)
  ingredient7 = Ingredient.objects.create(name="red chilli, finely sliced", unit="", base_quantity=1)
  ingredient8 = Ingredient.objects.create(name="vegetable oil", unit="tbsp", base_quantity=2)
  ingredient9 = Ingredient.objects.create(name="spring onions, finely sliced", unit="", base_quantity=2)

  recipe = Recipe.objects.create(
    name="Air Fryer Crispy Chilli Beef",
    category="Main course",
    difficulty="Medium",
    prep_time="15 minutes",
    cooking_time="10 minutes",
    base_servings=4,
    current_servings=4,
    pre_prep_instructions="Slice the beef into thin strips and pat dry."
    instructions="
    "Place the beef strips in a bowl, add cornflour, and toss to coat evenly.",
    "Preheat the air fryer to 200°C.",
    "Lightly spray the air fryer basket with oil and add the beef strips in a single layer.",
    "Cook for 8-10 minutes, shaking halfway through until crispy.",
    "In a separate bowl, mix soy sauce, sweet chilli sauce, rice vinegar, ketchup, and red chilli.",
    "Heat the sauce mixture in a pan until it starts to thicken.",
    "Add the cooked beef to the pan and toss to coat in the sauce.",
    "Garnish with spring onions before serving."
    "
    notes="Serve immediately with steamed rice or noodles for a delicious and crispy meal."
  )
