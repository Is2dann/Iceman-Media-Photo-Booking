from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=50, help_text="e.g. 1 hour, 2-3 days turnaround")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title