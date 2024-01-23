from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def home (request):
    name = 'Dany'
    return render(request, 'home.html', {name : name})