from django.shortcuts import render


def index(request):
	title = "MainPage"
	context = {
		'title': title,
	}
	return render(request, 'Forum/Main/index.html', context)


def post_detail(request):
	title = "Post Detail"
	context = {
		'title': title,
	}
	return render(request, 'Forum/Main/detail.html', context)


def posts(request):
	title = "Posts"
	context = {
		'title': title,
	}
	return render(request, 'Forum/Main/posts.html', context)
