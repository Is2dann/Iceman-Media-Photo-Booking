from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomRegisterForm


# Create your views here.


def index(request):
    
    return render(request, 'home/index.html', )


def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatic login after registration.
            messages.success(request, 'Hooray...Registration successful. Welcome and Thank You')
            return redirect('index')
        else:
            messages.error(request, 'Something is not right. Please check all the fields again.')
    else:
        form = CustomRegisterForm()

    return render(request, 'home/index.html', {'form': form})