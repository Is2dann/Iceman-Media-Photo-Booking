from django.urls import path
from . import views

urlpatterns = [
    path('booked_dates/', views.get_booked_dates, name='booked_dates'),
    path('manage-bookings/', views.manage_bookings, name='manage_bookings'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('', views.book_photoshoot, name='book_photoshoot'),
]
