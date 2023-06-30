import pytest
from django.urls import reverse
from api.models import Ingredient, Recipe
from api.serializers import IngredientSerializer, RecipeSerializer, RecipeDetailSerializer

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
    url = reverse('ingredients_detail_error', kwargs={'invalid_id': 'haha'})
    response = client.get(url)

    assert response.status_code == 400
    assert response.data['message'] == 'Invalid id data type: id must be an integer'

@pytest.mark.django_db(reset_sequences=True)
def test_get_recipes_detail(client, test_ingredients, test_recipes):
    url = reverse('recipes_detail', kwargs={'recipe_id': 21})
    response = client.get(url)

    recipe = Recipe.objects.get(id=21)
    expected_data = RecipeDetailSerializer(recipe).data
    
    assert response.status_code == 200
    assert response.data == expected_data

@pytest.mark.django_db(reset_sequences=True)
def test_get_recipes_detail_nonexistent_id_error(client, test_ingredients, test_recipes):
    url = reverse('recipes_detail', kwargs={'recipe_id': 999})
    response = client.get(url)

    assert response.status_code == 404
    assert response.data['message'] == 'Nonexistent id'

@pytest.mark.django_db(reset_sequences=True)
def test_get_recipes_detail_invalid_id_error(client, test_ingredients, test_recipes):
    url = reverse('recipes_detail_error', kwargs={'invalid_id': 'blah'})
    response = client.get(url)

    assert response.status_code == 400
    assert response.data['message'] == 'Invalid id data type: id must be an integer'

@pytest.mark.django_db(reset_sequences=True)
def test_get_ingredients_list_sort_category(client, test_ingredients):
    url = reverse('ingredients_list')
    response_monster = client.get(url, {'category': 'monsterparts'})
    response_critters = client.get(url, {'category': 'critters'})
    response_food = client.get(url, {'category': 'food'})
    
    monster = Ingredient.objects.filter(category='monster parts')
    expected_monster_data = IngredientSerializer(monster, many=True).data

    critters = Ingredient.objects.filter(category='critters')
    expected_critters_data = IngredientSerializer(critters, many=True).data

    food = Ingredient.objects.filter(category='food')
    expected_food_data = IngredientSerializer(food, many=True).data

    assert response_monster.status_code == 200
    assert response_monster.data == expected_monster_data
    assert response_critters.status_code == 200
    assert response_critters.data == expected_critters_data
    assert response_food.status_code == 200
    assert response_food.data == expected_food_data

    