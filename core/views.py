from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def visualiza_tabela(request):
    return HttpResponse("Hello World by Django")
