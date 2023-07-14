from django.urls import path
from .views import *
from api import views

urlpatterns = [
    path('indice/', views.index, name='index'),
    path('distancia/', views.distancia, name='distancia'),
    path('peligroso/', views.peligro, name='peligroso'),
    path('cercano/', views.cercano, name='cercano'),
    path('lejano/', views.lejano, name='lejano'),
    path('hoy/', views.hoy, name='hoy'),
]