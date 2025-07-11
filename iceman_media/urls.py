"""
URL configuration for iceman_media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('about/', include('about.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls')),
    # this path ensures favicon will show on the live website
    # (from stackoverflow)
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('assets/favicon/favicon.ico'))),
    path('portfolio/', include('portfolio.urls')),
    path('services/', include('services.urls')),
    path('', include('home.urls'), name='home-urls'),
]
