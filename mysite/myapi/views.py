from rest_framework import viewsets

from .serializers import categoriesSerializer, RecipeSerializer
from .models import categories, Recipes


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = categories.objects.all().order_by('id')
    serializer_class = categoriesSerializer



class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all().order_by('recipeId')
    serializer_class = RecipeSerializer
