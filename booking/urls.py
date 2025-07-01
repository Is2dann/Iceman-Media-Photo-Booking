from django.urls import path
from . import views

urlpatterns = [
    path('booked_dates/', views.get_booked_dates, name='booked_dates'),
    path('', views.book_photoshoot, name='book_photoshoot'),
]