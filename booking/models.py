from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    """
    Stores a single booking entry related to `:model:auth.User`
    """
    PHOTOSHOOT_CHOICES = [
        ('Animals', 'Pets & Wildlife'),
        ('Children', 'Children'),
        ('Commercial', 'Commercial'),
        ('Events', 'Events'),
        ('Family', 'Family'),
        ('Headshots', 'Headshots & Products'),
        ('Landscapes', 'Landscape & Property'),
        ('Vehicle', 'Vehicle'),
        ('Wedding', 'Weddings & Ceremonies'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    photoshoot_type = models.CharField(
        max_length=50, choices=PHOTOSHOOT_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        unique_together = ('date', 'time')  # This prevents double booking

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time} - {self.photoshoot_type}"
