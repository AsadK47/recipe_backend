from rest_framework import serializers
from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingredient
    fields = ['id', 'name', 'unit', 'base_quantity', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
  ingredients = IngredientSerializer(many=True)

  class Meta:
    model = Recipe
    fields = [
      'id', 'name', 'category', 'difficulty', 'prep_time', 'cooking_time',
      'base_servings', 'current_servings', 'ingredients', 'pre_prep_instructions',
      'instructions', 'notes'
    ]
