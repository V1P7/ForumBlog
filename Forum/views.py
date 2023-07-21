from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post
from .utils import update_views


def index(request):
	title = "MainPage"
	context = {
		'title': title,
	}
	return render(request, 'Forum/Main/index.html', context)


def post_detail(request, slug):
	title = "Post Detail"
	post = get_object_or_404(Post, slug=slug)
	context = {
		'title': title,
		'post': post,
	}
	update_views(request, post)
	return render(request, 'Forum/Main/detail.html', context)


def posts(request):
	title = "Posts"
	context = {
		'title': title,
	}
	return render(request, 'Forum/Main/posts.html', context)
