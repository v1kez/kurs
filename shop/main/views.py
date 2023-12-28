from django.shortcuts import render
from .models import *

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)

def info(request):
    return render(request, 'main/info.html')

def new_home(request):
    new=News.objects.order_by('-date')
    return  render(request, 'main/new_home.html',{'new':new})

def feedback_home(request):
    feedback = Feed.objects.order_by('-date')
    return  render(request, 'main/feedback_home.html',{'feedback':feedback})