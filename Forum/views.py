from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Author, Category, Post, Comment, Reply, User
from .utils import update_views


def home(request):
	title = "MainPage"
	forum = Category.objects.all()
	num_posts = Post.objects.all().count()
	num_users = User.objects.all().count()
	num_categories = forum.count()
	last_post = Post.objects.latest('date')
	
	context = {
		'title': title,
		'forum': forum,
		'num_posts': num_posts,
		'num_users': num_users,
		'num_categories': num_categories,
		'last_post': last_post,
	}
	return render(request, 'Forum/Main/index.html', context)


def post_detail(request, slug):
	title = "Post Detail"
	post = get_object_or_404(Post, slug = slug)
	author = Author.objects.get(user = request.user)
	
	if 'comment-form' in request.POST:
		comment = request.POST.get('comment')
		author = Author.objects.get(user = request.user)
		new_comment, created = Comment.objects.get_or_create(user = author, content = comment)
		post.comments.add(new_comment.id)
	
	if 'reply-form' in request.POST:
		reply = request.POST.get('reply')
		comment_id = request.POST.get('comment-id')
		comment_obj = Comment.objects.get(id = comment_id)
		new_reply, created = Reply.objects.get_or_create(user = author, content = reply)
		comment_obj.replies.add(new_reply.id)
	
	context = {
		'title': title,
		'post': post,
	}
	update_views(request, post)
	return render(request, 'Forum/Main/detail.html', context)


def posts(request, slug):
	title = "Posts"
	category = get_object_or_404(Category, slug = slug)
	posts = Post.objects.filter(approved = True, categories = category)
	paginator = Paginator(posts, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
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
			new_post = Post(user = author)
			form = PostForm(request.POST, instance = new_post)
			form.save()
			return redirect('home')
	
	context = {
		'form': form,
		'title': 'Create Post'
	}
	
	return render(request, 'Forum/Main/create_post.html', context)


def latest_posts(request):
	posts = Post.objects.all().filter(approved = True)
	context = {
		'posts': posts,
		'title': 'Latest 10 posts'
	           }
	return render(request, 'Forum/Main/latest_posts.html', context)
