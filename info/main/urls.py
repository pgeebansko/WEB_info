from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.info_main, name='home'),
]

# python -m pip install django-cors-headers