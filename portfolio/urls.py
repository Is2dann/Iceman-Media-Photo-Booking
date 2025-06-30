from django.urls import path
from . import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<slug:slug>/', views.category_gallery, name='category_gallery'),
    path('like/<int:image_id>/', views.toggle_like, name='like_photo'),
    path('comment/<int:image_id>/', views.add_comment, name='add_comment'),
]
