from rest_framework import generics
from rest_framework.response import Response
from .models import Ingredient, Recipe
from .serializers import IngredientSerializer, RecipeSerializer, RecipeDetailSerializer
from .api_exceptions import NonexistentIdException, InvalidIdException


class IngredientListView(generics.ListAPIView):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        queryset = Ingredient.objects.order_by('id')
        ingredient_category = self.request.query_params.get('category')

        if ingredient_category is not None:
            if ingredient_category == 'monsterparts':
                queryset = queryset.filter(category='monster parts')
            elif ingredient_category != "":
                queryset = queryset.filter(category=ingredient_category)
        
        return queryset

class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.order_by('id')
    serializer_class = RecipeSerializer

class IngredientDetailView(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get(self, request, ingredient_id):
        try:
            ingredient_id > Ingredient.objects.count()
            ingredient = Ingredient.objects.get(id=ingredient_id)
            return Response(IngredientSerializer(ingredient).data)
        except:
            raise NonexistentIdException()

class InvalidDetailView(generics.RetrieveAPIView):
    def get(self, request, invalid_id):
            raise InvalidIdException()

class RecipeDetailView(generics.RetrieveAPIView):
    queryset = Recipe.objects.order_by('id')
    serializer_class = RecipeDetailSerializer

    def get(self, request, recipe_id):
        try:
            recipe_id > Recipe.objects.count()
            recipe = Recipe.objects.get(id=recipe_id)
            return Response(RecipeDetailSerializer(recipe).data)
        except:
            raise NonexistentIdException()
