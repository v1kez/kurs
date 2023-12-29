from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('info/',views.info, name='info'),
   path('new/', views.new_home, name='new_home'),
   path('feedback/', views.feedback_home, name='feedback_home'),
   path('feedback/create',views.create, name='create')
]