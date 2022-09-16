from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def heet(request):
    return HttpResponse("Hello, Heet!")

def david(request):
    return(HttpResponse("Hello, David!"))