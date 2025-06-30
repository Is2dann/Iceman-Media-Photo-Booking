from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PortfolioImage(models.Model):
    category = models.ForeignKey(
        PortfolioCategory, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
