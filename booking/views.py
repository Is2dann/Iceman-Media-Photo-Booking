from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import BookingForm
from .models import Booking

# Create your views here.


@login_required
def book_photoshoot(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            # Check for double booking again to be sure
            if Booking.objects.filter(
                    date=booking.date).exists():
                messages.error(request, "Sorry, that day is already booked.")
            else:
                booking.save()
                messages.success(
                    request,
                    "Your booking request has been submitted." \
                    "I endeavor to respond within 2 days.")
                return redirect('book_photoshoot')
        else:
            print("Form errors:", form.errors)
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})


def get_booked_dates(request):
    dates = Booking.objects.values_list('date', flat=True)
    unique_dates = list(set(dates))  # Remove duplicates
    return JsonResponse({'booked_dates': unique_dates})


@staff_member_required
def manage_bookings(request):
    bookings = Booking.objects.all().order_by('-date', '-time')
    return render(
        request, 'booking/manage_bookings.html', {'bookings': bookings})
