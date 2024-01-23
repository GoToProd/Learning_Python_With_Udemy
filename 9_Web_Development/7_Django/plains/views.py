from django.shortcuts import render
from .models import Plains
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

__all__ = ( 'home',
            'PlainsListView',
            'PlainsDetailView',
            )


def home(request, pk = None):
    qs = Plains.objects.all()
    print(qs)
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'plains/main.html', context)


class PlainsDetailView(DetailView):
    queryset = Plains.objects.all()
    template_name = 'plains/detail.html'

class PlainsListView(ListView):
    paginate_by = 2
    model = Plains
    template_name = 'plains/home.html'