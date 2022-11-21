from django.shortcuts import render
from .models import Colaborator 


# Create your views here.

def colaborators(request):
    colaborators= Colaborator.objects.all()
    return render (request, "colaborators/colaborators.html",{'colaborators':colaborators})

