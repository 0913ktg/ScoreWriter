from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import path, include


def index(request):
    return render(request, "mainPage/index.html", {})

def score(request):
    return render(request, "mainPage/verovio.html", {})

