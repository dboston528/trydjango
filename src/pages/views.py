from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs): # *args, **kwargs is a python thing, know what it memans
    return HttpResponse ("<h1>Hello World</h1>") #string of html code