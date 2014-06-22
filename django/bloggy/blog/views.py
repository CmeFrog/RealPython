from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.template import Context, loader
from django.shortcuts import get_object_or_404

# Create your views here.
def index_id(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	t = loader.get_template('blog/index_id.html')
	c = Context({'latest_posts' : latest_posts,})
	return HttpResponse(t.render(c))
	
def index_url(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	t = loader.get_template('blog/index_url.html')
	context_dict = {'latest_posts' : latest_posts}
	for post in latest_posts:
		post.url = post.title.replace(' ', '_')
	c = Context({'latest_posts' : latest_posts,})
	return HttpResponse(t.render(c))
	
def post_id(request, post_id):
	single_post = get_object_or_404(Post, pk=post_id)
	t = loader.get_template('blog/post.html')
	c = Context({'single_post' : single_post})
	return HttpResponse(t.render(c))
	
def post_url(request, post_name):
	single_post = get_object_or_404(Post, title=post_name.replace('_', ' '))
	t = loader.get_template('blog/post.html')
	c = Context({'single_post' : single_post})
	return HttpResponse(t.render(c))
	
def jtn(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	t = loader.get_template('blog/jtn.html')
	context_dict = {'latest_posts' : latest_posts}
	for post in latest_posts:
		post.url = post.title.replace(' ', '_')
	c = Context({'latest_posts' : latest_posts,})
	return HttpResponse(t.render(c))
