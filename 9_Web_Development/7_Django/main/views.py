from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib import messages

from .models import City
from .forms import CityForm

__all__ = ('home', 
        'CityCreateView', 
        'CityDetailsView', 
        'CityUpdateView', 
        'CityDeleteView')

def home(request, pk = None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs,1)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': qs, 'form': form}
    return render(request, 'main/main.html', context)


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm 
    template_name = 'main/create.html'
    success_url = reverse_lazy('main:home')
    success_message = 'Город создан успешно'


class CityDetailsView(DetailView):
    queryset = City.objects.all()
    template_name = 'main/detail.html'


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'main/update.html'
    success_message = 'City Updated'
    success_url = reverse_lazy('main:home')


class CityDeleteView(SuccessMessageMixin, DeleteView):
    model = City
    template_name = 'main/delete.html'
    success_url = reverse_lazy('main:home')
    def get(self, request, *args, **kwargs):
        messages.success(request, 'City deleted successfully')
        return self.post(request, *args, **kwargs)
