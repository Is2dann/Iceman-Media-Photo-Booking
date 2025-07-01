from django.db import models

# Create your models here.


class Service(models.Model):
    """
    Stores a photography service offering, including title, description,
    pricing, and estimated delivery time.

    Fields:
        - title: Name of the service (e.g., "Wedding Photography")
        - description: Detailed description of what's included
        - price: Cost of the service, stored as a decimal value
        - duration: Expected duration or delivery time (e.g., "1 hour", "2–3 days turnaround")

    Meta:
        - Orders services alphabetically by title for consistent display
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(
        max_length=50, help_text="e.g. 1 hour, 2-3 days turnaround")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
