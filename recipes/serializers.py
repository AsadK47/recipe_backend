from rest_framework import serializers
from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    baseQuantity = serializers.FloatField(source='base_quantity')
    quantity = serializers.FloatField()
    unit = serializers.CharField()
    name = serializers.CharField()

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'unit', 'baseQuantity', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    prepTime = serializers.CharField(source='prep_time')
    cookingTime = serializers.CharField(source='cooking_time')
    baseServings = serializers.IntegerField(source='base_servings')
    currentServings = serializers.IntegerField(source='current_servings')
    prePrepInstructions = serializers.JSONField(source='pre_prep_instructions')

    class Meta:
        model = Recipe
        fields = [
            'id', 'name', 'category', 'difficulty', 'prepTime', 'cookingTime',
            'baseServings', 'currentServings', 'ingredients', 'prePrepInstructions',
            'instructions', 'notes'
        ]
