from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListView(APIView):
  def get(self, request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)
  
class RecipeDetailView(APIView):
  def get(self, request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    except Recipe.DoesNotExist:
      return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)
