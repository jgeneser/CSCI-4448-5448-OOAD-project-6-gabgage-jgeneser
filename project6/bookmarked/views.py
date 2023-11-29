from django.shortcuts import render
from django.http import Http404


# Create your views here.
from django.http import HttpResponse
from .models import Users

def index(request):
    return render(request, "bookmarked/index.html")

def login(request):
    return render(request, "bookmarked/login.html")

def signup(request):
    return render(request, "bookmarked/signup.html")

def homepage(request):
    return render(request, "bookmarked/homepage.html")

def shoppinglist(request):
    return render(request, "bookmarked/shoppinglist.html")

def addrecipe(request):
    return render(request, "bookmarked/addrecipe.html")