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
    """
    Handles the creation of a new booking by a logged-in user.

    - Accepts POST requests with booking form data.
    - Prevents double bookings by checking if the selected date already exists.
    - On success, saves the booking and redirects with a success message.
    - Displays form errors if validation fails.
    - Renders the booking form for GET requests.

    Template: booking/booking.html
    Context: {'form': BookingForm}
    """
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
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})


@login_required
def my_bookings(request):
    """
    Displays a list of all bookings made by the currently logged-in user.

    - Bookings are ordered by date in descending order.
    - Requires the user to be logged in.

    Template: booking/my_bookings.html
    Context: {'bookings': user’s bookings}
    """
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})


def get_booked_dates(request):
    """
    Returns a JSON response containing a list of all booked dates.

    - Used for disabling unavailable days in the booking form’s calendar.
    - Removes duplicate dates.

    Response: JSON with key 'booked_dates'
    Example: {'booked_dates': ['2025-07-01', '2025-07-03']}
    """
    dates = Booking.objects.values_list('date', flat=True)
    unique_dates = list(set(dates))  # Remove duplicates
    return JsonResponse({'booked_dates': unique_dates})


@staff_member_required
def manage_bookings(request):
    """
    Provides staff users with a management view of all bookings.

    - Bookings are shown in descending order by date and time.
    - Only accessible by staff users.

    Template: booking/manage_bookings.html
    Context: {'bookings': all bookings in the system}
    """
    bookings = Booking.objects.all().order_by('-date', '-time')
    return render(
        request, 'booking/manage_bookings.html', {'bookings': bookings})
