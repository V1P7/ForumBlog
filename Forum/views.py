from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
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
		'forum': category,
	}
	return render(request, 'Forum/Main/posts.html', context)


@login_required
def create_post(request):
	form = PostForm(request.POST or None)
	
	if request.method == 'POST':
		if form.is_valid():
			author = Author.objects.get(user = request.user)
			new_post = Post(user=author)
			form = PostForm(request.POST, instance = new_post)
			form.save()
			return redirect('home')
	
	context = {
		'form': form,
		'title': 'Create Post'
	}
	
	return render(request, 'Forum/Main/create_post.html', context)
