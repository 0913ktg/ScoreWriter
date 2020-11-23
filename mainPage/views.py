from django.shortcuts import render
from .score_module import * 

# Create your views here.
from django.http import HttpResponse
from django.urls import path, include


def index(request):
    return render(request, "mainPage/index.html", {})

def score(request):
    clearData()
    input = '../Module/data/flap.wav'  # 추후 사용자가 업로드 한 파일을 불러올 예정
    add_file(input)
    return render(request, "mainPage/verovio.html", {})