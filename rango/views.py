from django.shortcuts import render #remove?

# Create your views here
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!")
