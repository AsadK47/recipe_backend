from django.contrib import admin
from .models import Recipe, Ingredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
  list_display = ('name', 'category', 'difficulty', 'prep_time', 'cooking_time')
  search_fields = ('name', 'category')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
  list_display = ('name', 'unit', 'base_quantity')
  search_fields = ('name',)
