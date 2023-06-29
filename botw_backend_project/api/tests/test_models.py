import pytest

from api.models import Ingredient, Recipe

@pytest.mark.django_db
def test_create_ingredient():
    Ingredient.objects.create(
        category='food', 
        duration='2:00',
        hearts='1', 
        name='Silent Princess', 
        resale='10', 
        type='Green')
    
    assert Ingredient.objects.count() == 1

@pytest.mark.django_db
def test_create_recipe():
    ingredient = Ingredient.objects.create(
        category='food', 
        duration='2:00',
        hearts='1', 
        name='Silent Princess', 
        resale='10', 
        type='Green')
    
    Recipe.objects.create(
        category="recipe",
        duration="10:00",
        hearts="10",
        ingredient1=ingredient,
        ingredient2=ingredient,
        ingredient3=ingredient,
        ingredient4=ingredient,
        ingredient5=ingredient,
        name="Sneaky Fried Wild Greens",
        resale="140",
        strength="High",
        type="Stealth"
    )
    
    assert Recipe.objects.count() == 1
