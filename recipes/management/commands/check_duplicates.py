from django.core.management.base import BaseCommand
from django.db.models import Count
from recipes.models import Recipe, Ingredient

class Command(BaseCommand):
  help = "Check for duplicate recipes in the database"

  def handle(self, *args, **kwargs):
    duplicates = Recipe.objects.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)

    if duplicates.exists():
      self.stdout.write("Duplicate recipes found:")
      for duplicate in duplicates:
        self.stdout.write(f"Name: {duplicate['name']}, Count: {duplicate['name_count']}")
    else:
      self.stdout.write("No duplicates found!")
