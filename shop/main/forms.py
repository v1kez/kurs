from .models import Feed
from django.forms import ModelForm, TextInput, DateTimeInput,Textarea

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