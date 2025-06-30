from django.shortcuts import render
from .models import Service

# Create your views here.


def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})