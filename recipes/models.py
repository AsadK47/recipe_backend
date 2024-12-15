import uuid
from django.db import models

class Ingredient(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  base_quantity = models.FloatField()
  quantity = models.FloatField(blank=True, null=True)
  unit = models.CharField(max_length=50)
  name = models.CharField(max_length=255)

  def save(self, *args, **kwargs):
    if self.quantity is None:
      self.quantity = self.base_quantity
    super().save(*args, **kwargs)
  
  def __str__(self):
    return f"{self.name} ({self.base_quantity} {self.unit})"

class Recipe(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=255)
  category = models.CharField(max_length=100)
  difficulty = models.CharField(max_length=50)
  prep_time = models.CharField(max_length=50)
  cooking_time = models.CharField(max_length=50)
  base_servings = models.IntegerField()
  current_servings = models.IntegerField()
  ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
  pre_prep_instructions = models.TextField()
  instructions = models.TextField()
  notes = models.TextField(blank=True)

  def __str__(self):
    return self.name
