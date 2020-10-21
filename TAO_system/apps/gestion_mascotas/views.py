from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#E para mostrar el elemnto index
def index(request):
    return HttpResponse("Index")