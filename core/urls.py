from django.urls import path
from . import views

urlpatterns = [
    path('visualiza-tabela', views.visualiza_tabela, name='visualiza_tabela'),
]