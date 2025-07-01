from django.contrib import admin
from .models import Booking

# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'photoshoot_type',
        'message', 'date', 'time',
        'status', 'status_message',
        'created_on'
    )
    list_filter = ('status', 'date', 'photoshoot_type', 'is_approved')
    # This way bookings can be approved and messaged 
    # straight from admin table, don't need to open them.
    list_editable = (
        'status',
        'status_message'
    )
    ordering = ('-date',)
