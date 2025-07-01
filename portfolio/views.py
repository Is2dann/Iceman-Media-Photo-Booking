from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
        request, 'portfolio/portfolio.html', {
            'showcase_items': showcase_items})


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
        f"{request.META.get('HTTP_REFERER', '')}#image{image.id}")


@login_required
def add_comment(request, image_id):
    if request.method == "POST":
        image = get_object_or_404(PortfolioImage, id=image_id)
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                image=image, user=request.user, content=content)
    return HttpResponseRedirect(
        f"{request.META.get('HTTP_REFERER', '')}#image{image_id}")


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    """
    Only allow the user who commented to edit it
    """
    if comment.user != request.user:
        messages.error(request, "You are not allowed to edit this comment.")

    if request.method == "POST":
        new_content = request.POST.get('content', '').strip()
        if new_content:
            comment.content = new_content
            comment.save()
            messages.success(request, "Your comment has been updated.")
        else:
            messages.error(request, "Comment cannot be empty.")
        return HttpResponseRedirect(
            f"{request.META.get('HTTP_REFERER', '')}#image{comment.image.id}")


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    """
    Only allow the user who commented to delete it
    """
    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Your comment was deleted.")
    else:
        messages.error(
            request, "You are not authorized to delete this comment.")

    return HttpResponseRedirect(
        f"{request.META.get('HTTP_REFERER', '')}#image{comment.image.id}")
