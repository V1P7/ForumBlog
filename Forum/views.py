from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post
from .utils import update_views


def home(request):
	title = "MainPage"
	forum = Category.objects.all()
	context = {
		'title': title,
		'forum': forum,
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


def posts(request, slug):
	title = "Posts"
	category = get_object_or_404(Category,slug=slug)
	posts = Post.objects.filter(approved = True, categories = category)
	context = {
		'title': title,
		'posts': posts,
	}
	return render(request, 'Forum/Main/posts.html', context)
