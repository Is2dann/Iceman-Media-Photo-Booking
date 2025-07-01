from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import PortfolioCategory, PortfolioImage, Comment, Like

# Create your views here.


def portfolio(request):
    """
    Displays the main portfolio page with a showcase grid.

    - Retrieves all portfolio categories and their associated images.
    - For each category, selects the first image as a visual representative.
    - Passes category-image pairs to the template for display.

    Template: portfolio/portfolio.html
    Context: {'showcase_items': [{'category': ..., 'image': ...}, ...]}
    """
    categories = PortfolioCategory.objects.prefetch_related('images')
    showcase_items = []
    for category in categories:
        image = category.images.first()
        if image:
            showcase_items.append({'category': category, 'image': image})

    return render(
        request, 'portfolio/portfolio.html', {
            'showcase_items': showcase_items})


def category_gallery(request, slug):
    """
    Displays all images in a given portfolio category.

    - Uses the slug to find the matching PortfolioCategory.
    - Fetches all images related to that category.

    Template: portfolio/category_gallery.html
    Context: {'category': category, 'images': images}
    """
    category = get_object_or_404(PortfolioCategory, slug=slug)
    images = category.images.all()

    return render(request, 'portfolio/category_gallery.html', {
        'category': category,
        'images': images
    })


@login_required
def toggle_like(request, image_id):
    """
    Toggles a 'like' for a portfolio image.

    - If the user has not liked the image, a new Like is created.
    - If a like already exists, it is removed.
    - Redirects the user back to the referring page with anchor to the image.

    Redirect: Back to the same category page with anchor (e.g. #image3)
    """
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
    """
    Adds a new comment to a portfolio image.

    - Accepts POST data with comment content.
    - Creates a new Comment instance if content is valid.
    - Redirects back to the referring page anchored to the image.

    Redirect: Back to the same category page with anchor (e.g. #image3)
    """
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
    """
    Allows a user to edit their own comment.

    - Verifies that the logged-in user is the owner of the comment.
    - Updates the comment content on POST if non-empty.
    - Displays appropriate success or error messages.

    Redirect: Back to the same category page with anchor (e.g. #image3)
    """
    comment = get_object_or_404(Comment, id=comment_id)
    
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
    """
    Allows a user to delete their own comment.

    - Verifies ownership before deletion.
    - Displays confirmation or error messages.
    - Redirects back to the same category page with anchor.

    Redirect: Back to the same category page with anchor (e.g. #image3)
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Your comment was deleted.")
    else:
        messages.error(
            request, "You are not authorized to delete this comment.")

    return HttpResponseRedirect(
        f"{request.META.get('HTTP_REFERER', '')}#image{comment.image.id}")
