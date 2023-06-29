from rest_framework import serializers
from .models import Ingredient, Recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'category', 'duration', 'effect', 'hearts', 'name', 'resale', 'type', 'image']

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'image']

class RecipeSerializer(serializers.ModelSerializer):
    ingredient1 = RecipeIngredientSerializer()
    ingredient2 = RecipeIngredientSerializer()
    ingredient3 = RecipeIngredientSerializer()
    ingredient4 = RecipeIngredientSerializer()
    ingredient5 = RecipeIngredientSerializer()

    class Meta:
        model = Recipe
        fields = ['id', 'category', 'name', 'duration', 'hearts','strength', 'type', 'image', 'type_image', 'ingredient1', 'ingredient2', 'ingredient3', 'ingredient4', 'ingredient5', 'notes', 'resale']

class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredient1 = IngredientSerializer()
    ingredient2 = IngredientSerializer()
    ingredient3 = IngredientSerializer()
    ingredient4 = IngredientSerializer()
    ingredient5 = IngredientSerializer()

    class Meta:
        model = Recipe
        fields = ['id', 'category', 'name', 'duration', 'hearts','strength', 'type', 'image', 'type_image', 'ingredient1', 'ingredient2', 'ingredient3', 'ingredient4', 'ingredient5', 'notes', 'resale']