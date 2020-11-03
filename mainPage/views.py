from django.shortcuts import render
from .score_module import * 

# Create your views here.
from django.http import HttpResponse
from django.urls import path, include


def index(request):
    return render(request, "mainPage/index.html", {})

def score(request):
    # clearData()
    # add_file('test')
    return render(request, "mainPage/verovio.html", {})