from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
path('', home, name='home'),
path('add/', CityCreateView.as_view(), name = "create"),
path('detail/<int:pk>', CityDetailsView.as_view(), name = "detail"),
path('update/<int:pk>', CityUpdateView.as_view(), name = "update"),
path('delete/<int:pk>', CityDeleteView.as_view(), name = "delete")
]  