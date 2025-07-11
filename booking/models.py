from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    """
    Stores a single booking request submitted by a user.

    Related to:
        - :model:`auth.User`

    Includes details such as:
        - Full name, email, phone number
        - Photoshoot type from a predefined list
        - Preferred date and time
        - Optional message to the photographer
        - Approval status and admin feedback

    Enforces:
        - Unique booking per date and time
        - Admin-only status update workflow
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

    STATUS_CHOICES = [
        ('pending', 'Pending',),
        ('approved', 'Approved',),
        ('rejected', 'Rejected',),
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
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    status_message = models.TextField(blank=True)

    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        unique_together = ('date', 'time')  # This prevents double booking

    def __str__(self):
        return f"{
            self.user.username} - {
                self.date} {self.time} - {self.photoshoot_type}"
