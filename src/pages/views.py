from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs): # *args, **kwargs is a python thing, know what it memans
    print(args, kwargs)
    print(request.user)
    # return HttpResponse ("<h1>Hello World</h1>") #string of html code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>This is a social view</h1>")