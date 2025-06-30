from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

# Create your models here.


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Converting the name into a URL safe format
        super().save(*args, **kwargs)  # Overrides the default save method to automatically generate the slug when saving a category

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
