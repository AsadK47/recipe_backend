from django.core.management.base import BaseCommand
from recipes.models import Recipe, Ingredient
from recipes.management.commands.seed_data import Command as SeedCommand

class Command(BaseCommand):
  help = "Reset the database and seed it with recipes and ingredients"

  def handle(self, *args, **kwargs):
    try:
        self.stdout.write("Clearing existing data...")
        Recipe.objects.all().delete()
        Ingredient.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Existing data cleared successfully"))
        seed_command = SeedCommand()
        seed_command.handle()

        self.stdout.write(self.style.SUCCESS("Database has been reset and seeded successfully!"))
    
    except Exception as e:
       self.stderr.write(self.style.ERROR(f"Error during reset and seeding: {e}"))
