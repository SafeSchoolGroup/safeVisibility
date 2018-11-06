from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Classe


def home(request):
    classes = Classe.objects.all()
    return render(request, 'home.html', {'classes': classes})
