
# Register your models here.
from django.contrib import admin

from .models import Users

admin.site.register(Users)

from .models import Recipes

admin.site.register(Recipes)