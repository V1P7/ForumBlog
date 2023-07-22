from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug>/', views.posts, name='posts'),
]
