from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Feed
from django.forms import ModelForm, TextInput, DateTimeInput,Textarea

User = get_user_model()
class FeedForm(ModelForm):
    class Meta:
        model=Feed
        fields=['fio','text','date']

        widgets={
            "fio": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            })
        }


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
