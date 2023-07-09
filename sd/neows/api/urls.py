from django.urls import path
from .views import *
from api import views

urlpatterns = [
    path('test/', views.NeoWSViewTest.as_view(), name='test'),
    path('neows/', views.NeoWSView.as_view(), name='neows'),
    #path('neows/<str:init_date>/<str:end_date>/<str:key>', views.NeoWSView.as_view(), name='neows'),
]