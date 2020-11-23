from django.shortcuts import render
from .score_module import *

# Create your views here.
from django.http import HttpResponse
from django.urls import path, include


def index(request):
    return render(request, "mainPage/index.html", {})


def score(request):
    clearData()
    # input = '../Module/data/flap.wav'  # 추후 사용자가 업로드 한 파일을 불러올 예정

    print(request.POST.get('youtube_link'))
    if request.POST.get('youtube_link') == '':
        print('파일 업로드')
        input = request.FILES['upload_file']
        add_file(input)
    else:
        print('링크 업로드')
        pass
    return render(request, "mainPage/verovio.html", {})
