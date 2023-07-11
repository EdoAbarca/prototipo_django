from django.urls import path
from .views import *
from api import views

urlpatterns = [
    path('test/', views.NeoWSViewTest.as_view(), name='test'),
    path('indice/', views.index, name='index'),
    path('distancia/', views.distancia, name='distancia'),
    path('acercandose/', views.acercandose, name='acercandose'),
    path('cercano/', views.cercano, name='cercano'),
    path('lejano/', views.lejano, name='lejano'),
    path('hoy/', views.hoy, name='hoy'),
    path('neows/', views.NeoWSView.as_view(), name='neows'),
    #path('neows/<str:init_date>/<str:end_date>/<str:key>', views.NeoWSView.as_view(), name='neows'),
]