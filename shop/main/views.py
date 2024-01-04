from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .models import *
from .forms import FeedForm, UserCreationForm
from .utils import DataMixin


def index(request):

    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data, )

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

def buy(request):
    return render(request, 'main/buy.html')

def vce(request):
    return render(request, 'main/vce.html')




class Register(View):
    template_name = 'registration/register.html'
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate( username=username, password=password)
            login(request,user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)