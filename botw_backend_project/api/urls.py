from django.urls import path
from .views import IngredientListView, RecipeListView, IngredientDetailView, InvalidIngredientDetailView

urlpatterns = [
    path('ingredients', IngredientListView.as_view(), name='ingredients_list'),
    path('recipes', RecipeListView.as_view(), name='recipes_list'),
    path('ingredients/<int:ingredient_id>', IngredientDetailView.as_view(), name='ingredients_detail' ),
    path('ingredients/<str:ingredient_id>', InvalidIngredientDetailView.as_view(), name='ingredients_detail_error')

]