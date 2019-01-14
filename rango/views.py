from django.shortcuts import render #remove?

# Create your views here
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! Go to about page: <br/> <a href='/rango/about/'>About</a> ")
    # <br/> new line
    # <a href='/rango/about/'>About</a> link to rango/about. The link is shown as About


def about(request):
    return HttpResponse("Rango says here is the about page. Go back: <a href='/rango/'>Index</a> ")
