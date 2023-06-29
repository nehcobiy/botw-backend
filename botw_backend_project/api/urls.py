from django.urls import path
from .views import IngredientListView, RecipeListView, IngredientDetailView, InvalidDetailView, RecipeDetailView

urlpatterns = [
    path('ingredients', IngredientListView.as_view(), name='ingredients_list'),
    path('recipes', RecipeListView.as_view(), name='recipes_list'),
    path('ingredients/<int:ingredient_id>', IngredientDetailView.as_view(), name='ingredients_detail' ),
    path('ingredients/<str:invalid_id>', InvalidDetailView.as_view(), name='ingredients_detail_error'),
    path('recipes/<int:recipe_id>', RecipeDetailView.as_view(), name='recipes_detail' ),
    path('recipes/<str:invalid_id>', InvalidDetailView.as_view(), name='recipes_detail_error'),
]