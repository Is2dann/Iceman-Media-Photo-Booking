from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Creates a form from the model.
    with the widgets enhances UX, and
    uses a date/time picker.
    """
    class Meta:
        model = Booking
        fields = ['photoshoot_type', 'date', 'time', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
