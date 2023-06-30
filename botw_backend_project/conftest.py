import pytest
from api.models import Ingredient, Recipe
import json
import os
from rest_framework.test import APIClient

ingredients_data_path = os.path.join(os.path.dirname(__file__), "api/data/test/test-ingredients.json")
ingredients = json.load(open(ingredients_data_path))

recipes_data_path = os.path.join(os.path.dirname(__file__), "api/data/test/test-recipes.json")
recipes = json.load(open(recipes_data_path))

@pytest.fixture
def test_ingredients():
    ingredient_list = []
    for ingredient in ingredients:
        test_ingredient = Ingredient.objects.get_or_create(category=ingredient['category'],duration=ingredient['duration'], effect=ingredient['effect'], hearts=ingredient['hearts'], name=ingredient['name'], resale=ingredient['resale'], type=ingredient['type'], image=ingredient['image'] )

        ingredient_list.append(test_ingredient)
    
    return ingredient_list

@pytest.fixture
def test_recipes():
    recipe_list = []
    for recipe in recipes:
        i1 = Ingredient.objects.get(name=recipe['ingredient1'])
        try:
            i2 = Ingredient.objects.get(name=recipe['ingredient2'])
        except:
            i2 = None
        
        try:
            i3 = Ingredient.objects.get(name=recipe['ingredient3'])
        except:
            i3 = None
        
        try:
            i4 = Ingredient.objects.get(name=recipe['ingredient3'])
        except:
            i4 = None

        try:
            i5 = Ingredient.objects.get(name=recipe['ingredient3'])
        except:
            i5 = None
        
        try:
            recipe_duration = recipe['duration']
        except:
            recipe_duration = None

        try:
            recipe_strength = recipe['strength']
        except:
            recipe_strength = None

        test_recipe = Recipe.objects.get_or_create(category=recipe['category'], duration=recipe_duration, hearts=recipe['hearts'], notes=recipe['notes'], resale=recipe['resale'], strength=recipe_strength, type=recipe['type'], image=recipe['image'], type_image=recipe['type_image'], name=recipe['name'], ingredient1=i1, ingredient2=i2, ingredient3=i3, ingredient4=i4, ingredient5=i5)
        
        recipe_list.append(test_recipe)    
    
    return recipe_list

