from django.urls import path
from . import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<slug:slug>/', views.category_gallery, name='category_gallery'),
]
