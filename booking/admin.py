from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'photoshoot_type', 'date', 'time', 'created_on')
    list_filter = ('date', 'photoshoot_type')
    ordering = ('-date',)