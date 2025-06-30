from django.urls import path
from . import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<slug:slug>/', views.category_gallery, name='category_gallery'),
    path('comment/<int:image_id>/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('like/<int:image_id>/', views.toggle_like, name='like_photo'),
]
