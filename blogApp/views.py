from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "blogApp/home.html")


def hello():
    return HttpResponse("<h1>Cohort 13</h1>")


def greet():
    return HttpResponse("Welcome to django")


def simi(request):
    return render(request, 'blogApp/simex.html')
