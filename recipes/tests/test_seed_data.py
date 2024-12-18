from django.test import TestCase
from recipes.models import Recipe, Ingredient
from recipes.management.commands.seed_data import Command

class SeedDataTest(TestCase):
  def test_seed_data_creates_recipes_and_ingredients(self):
    command = Command()
    command.handle()

    recipes = Recipe.objects.all()
    ingredients = Ingredient.objects.all()

    self.assertEqual(len(recipes), 2)
    self.assertGreater(len(ingredients), 0)

    for recipe in recipes:
      self.assertGreater(len(recipe.ingredients.all()), 0)
