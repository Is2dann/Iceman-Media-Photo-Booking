from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def im_home(request):
    return HttpResponse("Hello there, I'm Obi-Wan Kenobi.")
