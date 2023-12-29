from django.shortcuts import render, redirect
from .models import *
from .forms import FeedForm


def index(request):
    index = Product.objects.order_by('price')
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data, {'index':index})

def info(request):
    return render(request, 'main/info.html')

def new_home(request):
    new=News.objects.order_by('-date')
    return  render(request, 'main/new_home.html',{'new':new})

def feedback_home(request):
    feedback = Feed.objects.order_by('-date')
    return  render(request, 'main/feedback_home.html',{'feedback':feedback})

def create(request):
    error=''
    if request.method == 'POST':
        form= FeedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_home')
        else:
            error='Форма была неверной'

    form=FeedForm()

    data ={
        'form': form,
        'error': error
    }

    return render(request, 'main/create.html',data)