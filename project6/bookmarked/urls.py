from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /polls/
    path("bookmarked/login", views.login, name="login"),
    path("bookmarked/signup", views.signup, name="signup"),    
    path("bookmarked/homepage", views.homepage, name="homepage"),
    path("bookmarked/shoppinglist", views.shoppinglist, name="shoppinglist"),
    path("bookmarked/addrecipe", views.addrecipe, name="addrecipe"),

]