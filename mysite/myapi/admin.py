from django.contrib import admin

# Register your models here.
from .models import categories
from .models import Recipes
admin.site.register(categories)
admin.site.register(Recipes)