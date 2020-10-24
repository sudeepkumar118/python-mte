from rest_framework import serializers

from .models import categories

from .models import Recipes

class categoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = categories
        fields = ('id','name', 'photo_url')

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipes
        fields = ('recipeId', 'categoryId', 'title', 'photo_url', 'photosArray', 'time', 'ingredients', 'description')