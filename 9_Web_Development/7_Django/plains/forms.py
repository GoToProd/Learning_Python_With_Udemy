from django import forms

from .models import Plains
from main.models import City

class PlainForm(forms.ModelForm):
    name = forms.CharField(label='Номер самолета', widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите номер самолета',
        }))
    travel_time = forms.IntegerField(label = 'Время в пути', widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Время в пути',
        }))
    fromCity = forms.ModelChoiceField(label = 'Город отправления', queryset=City.objects.all(), widget = forms.Select(attrs={
        'class': 'form-control',
        }))
    toCity = forms.ModelChoiceField(label = 'Город прибытия', queryset=City.objects.all(), widget = forms.Select(attrs={
        'class': 'form-control',
        }))
    
    class Meta:
        models = Plains
        fields = '__all__'
        