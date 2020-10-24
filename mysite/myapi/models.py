from django.db import models

# Create your models here.
class categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    photo_url = models.CharField(max_length=120)    
    
    def __str__(self):
        return self.name

class Recipes(models.Model):
    recipeId = models.AutoField(primary_key=True)
    categoryId = models.IntegerField()
    title =  models.CharField(max_length=120)  
    photo_url = models.CharField(max_length=120) 
    photosArray = models.TextField()  
    time = models.IntegerField()
    ingredients = models.TextField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title