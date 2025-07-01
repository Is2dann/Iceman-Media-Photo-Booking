from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomRegisterForm


# Create your views here.


def index(request):
    return render(request, 'home/index.html', )


def register(request):
    """
    Handles new user registration.

    - Displays a registration form (GET).
    - On POST, validates and creates a new user account.
    - Automatically logs in the user on successful registration.
    - Displays success or error messages accordingly.

    Template: home/register.html
    Context: {'form': CustomRegisterForm}
    Redirect: to 'index' on successful registration
    """
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatic login after registration.
            messages.success(
                request,
                'Hooray...Registration successful. Welcome and Thank You')
            return redirect('index')  # Redirects the user to the index page
        else:
            messages.error(
                request,
                'Something is not right. Please check all the fields again.')
    else:
        form = CustomRegisterForm()

    return render(request, 'home/register.html', {'form': form})


def user_login(request):
    """
    Handles user login.

    - Displays a login form (GET).
    - On POST, authenticates the user credentials.
    - Logs in the user and shows success message on success.
    - Displays error messages on failure.

    Template: home/login.html
    Context: {'form': AuthenticationForm}
    Redirect: to 'index' on successful login
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(
                request,
                f"Welcome back friend, {user.username}!")
            return redirect('index')
        else:
            messages.error(
                request,
                'Invalid username or password, please try again!')
    else:
        form = AuthenticationForm
    return render(request, 'home/login.html', {'form': form})


def user_logout(request):
    """
    Logs the user out and redirects to the homepage.

    - Clears the session and logs the user out.
    - Displays an informational message after logout.

    Redirect: to 'index' after logout
    """
    logout(request)
    messages.info(
        request,
        'You have been logged out. We miss you already!')
    return redirect('index')
