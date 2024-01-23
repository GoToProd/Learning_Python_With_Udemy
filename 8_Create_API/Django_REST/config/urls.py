"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from posts.views import *


router = routers.DefaultRouter()
router.register(r'Data', BlogViewSet)

print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
    
    # path('api/v1/', BlogViewSet.as_view({'get': 'list'})), # Get and Post
    # path('api/v1/<int:pk>', BlogViewSet.as_view({'put': 'update'})), # Put and Patch
    # path('api/v1/<int:pk>/delete', BlogViewSet.as_view({'delete': 'delete'})), # Get and Delete

    # path('api/v1/', PostsApiList.as_view()),
    # path('api/v1/<int:pk>', PostsUpdate.as_view()),
    # path('api/v1/<int:pk>/delete', PostsDetail.as_view()),
    # path('api/v1/', BlogApi.as_view()),
    # path('api/v1/<int:pk>', BlogApi.as_view()),
]
