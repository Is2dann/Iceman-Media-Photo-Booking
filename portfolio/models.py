from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class PortfolioCategory(models.Model):
    """
    Stores a single category in the database with a name and an automated slug.
    Slugify is Converting the name into a URL safe format.
    super().save: Overrides the default save method to automatically
        generate the slug when saving a category
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PortfolioImage(models.Model):
    """
    Stores a single image in the database with the category id as foreignkey,
    a title, the image and a DateTimeStamp.
    """
    category = models.ForeignKey(
        PortfolioCategory, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Stores a comment made by a user on a portfolio image
    """
    image = models.ForeignKey(
        'PortfolioImage', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.image.title}"


class Like(models.Model):
    """
    Stores likes from users on portfolio images (one like per user per image)
    unique_together prevents duplicate likes
    """
    image = models.ForeignKey(
        'PortfolioImage', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('image', 'user')

    def __str__(self):
        return f"{self.user.username} liked {self.image.title}"
