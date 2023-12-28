from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)

def info(request):
    return render(request, 'main/info.html')

def new_home(request):
    return  render(request, 'main/new_home.html')

def feedback_home(request):
    return  render(request, 'main/feedback_home.html')