import pytest
from django.urls import reverse
from api.models import Ingredient, Recipe
from api.serializers import IngredientSerializer, RecipeSerializer

@pytest.mark.django_db(reset_sequences=True)
def test_get_ingredients_list(client, test_ingredients):
    url = reverse('ingredients_list')
    response = client.get(url)

    ingredients = Ingredient.objects.all()
    expected_data = IngredientSerializer(ingredients, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data

@pytest.mark.django_db(reset_sequences=True)
def test_get_recipes_list(client, test_ingredients, test_recipes):
    url = reverse('recipes_list')
    response = client.get(url)

    recipes = Recipe.objects.all()
    expected_data = RecipeSerializer(recipes, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data

@pytest.mark.django_db(reset_sequences=True)
def test_get_ingredients_detail(client, test_ingredients):
    url = reverse('ingredients_detail', kwargs={'ingredient_id': 32})
    response = client.get(url)

    ingredient = Ingredient.objects.get(id=32)
    expected_data = IngredientSerializer(ingredient).data
    
    assert response.status_code == 200
    assert response.data == expected_data

@pytest.mark.django_db(reset_sequences=True)
def test_get_ingredients_detail_nonexistent_id_error(client, test_ingredients):
    url = reverse('ingredients_detail', kwargs={'ingredient_id': 300})
    response = client.get(url)

    assert response.status_code == 404
    assert response.data['message'] == 'Nonexistent id'

@pytest.mark.django_db(reset_sequences=True)
def test_get_ingredients_detail_invalid_id_error(client, test_ingredients):
    url = reverse('ingredients_detail_error', kwargs={'ingredient_id': 'haha'})
    response = client.get(url)

    assert response.status_code == 400
    assert response.data['message'] == 'Invalid id data type: id must be an integer'
   

