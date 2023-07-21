from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.post_detail, name='post_detail'),
    path('posts/', views.posts, name='posts'),
]
