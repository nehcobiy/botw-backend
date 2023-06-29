from rest_framework import generics
from rest_framework.response import Response
from .models import Ingredient, Recipe
from .serializers import IngredientSerializer, RecipeSerializer
from .api_exceptions import NonexistentIdException, InvalidIdException


class IngredientListView(generics.ListAPIView):
    queryset = Ingredient.objects.order_by('id')
    serializer_class = IngredientSerializer

class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer

class IngredientDetailView(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get(self, request, ingredient_id):
        try:
            ingredient_id > Recipe.objects.count()
            ingredient = Ingredient.objects.get(id=ingredient_id)
            return Response(IngredientSerializer(ingredient).data)
        except:
            raise NonexistentIdException()

class InvalidIngredientDetailView(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
    def get(self, request, ingredient_id):
        try:
            int(ingredient_id)
        except:
            raise InvalidIdException()