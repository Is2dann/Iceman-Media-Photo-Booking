from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import PortfolioCategory, PortfolioImage, Comment, Like

# Create your views here.


def portfolio(request):
    categories = PortfolioCategory.objects.prefetch_related('images')
    """
    Grab first image of each category (if available)
    """
    showcase_items = []
    for category in categories:
        image = category.images.first()
        if image:
            showcase_items.append({'category': category, 'image': image})

    return render(
        request, 'portfolio/portfolio.html', {'showcase_items': showcase_items})


def category_gallery(request, slug):
    category = get_object_or_404(PortfolioCategory, slug=slug)
    images = category.images.all()

    return render(request, 'portfolio/category_gallery.html', {
        'category': category,
        'images': images
    })


@login_required
def toggle_like(request, image_id):
    image = get_object_or_404(PortfolioImage, id=image_id)
    like, created = Like.objects.get_or_create(user=request.user, image=image)

    # If like already exists, delete it (toggle)
    # (from Django docs and stackoverflow)
    if not created:
        like.delete()

    return HttpResponseRedirect(
        request.META.get('HTTP_REFERER', reverse('portfolio')))


@login_required
def add_comment(request, image_id):
    if request.method == "POST":
        image = get_object_or_404(PortfolioImage, id=image_id)
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                image=image, user=request.user, content=content)
    return HttpResponseRedirect(
        request.META.get('HTTP_REFERER', reverse('portfolio')))
