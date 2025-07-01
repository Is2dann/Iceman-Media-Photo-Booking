from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'photoshoot_type', 'date', 'time', 'is_approved', 'created_on')
    list_filter = ('date', 'photoshoot_type', 'is_approved')
    list_editable = ('is_approved',)  # This way bookings can be approved straight from admin table
    ordering = ('-date',)
