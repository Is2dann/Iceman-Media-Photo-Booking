from django.shortcuts import render, get_object_or_404
from .models import PortfolioCategory

# Create your views here.


def portfolio(request):
    categories = PortfolioCategory.objects.prefetch_related('images')

    # Grab first image of each category (if available)
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