from django.shortcuts import render
from.forms import *
# Create your views here.
def vista_about(request):
    return render(request,'about.html')

def vista_contacto(request):
    formulario=contacto_form()
    nombre='Jose'
    return render(request,'contacto.html',{'nombre':nombre,'formulario':formulario})

def vista_servicios(request):
    return render(request,'servicios.html')