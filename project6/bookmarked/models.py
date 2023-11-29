from django.db import models

# Create your models here.

class Users(models.Model):
    #Primary Key?
    user_id = models.IntegerField
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    #Need to hash and salt
    password = models.CharField(max_length=200)



class Recipes(models.Model):
    #Primary key?
    recipe_id = models.IntegerField
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    directions = models.CharField(max_length=1000)