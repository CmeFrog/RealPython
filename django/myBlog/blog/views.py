from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect

from blog.models import Post
from blog.forms import PostForm

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
	
def index_url_styles(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	popular_posts = Post.objects.order_by('-views')[:5]
	t = loader.get_template('blog/index_url_styles.html')
	context_dict = {'latest_posts' : latest_posts, 'popular_posts' : popular_posts,}
	for post in latest_posts:
		post.url = encode_url(post.title)
	for post in popular_posts:
		post.url = encode_url(post.title)
	c = Context(context_dict)
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
	
def post_url_styles(request, post_name):
	single_post = get_object_or_404(Post, title=post_name.replace('_', ' '))
	t = loader.get_template('blog/post_styles.html')
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

def add_post(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit = True) #save form data to database
			return redirect(index_url_styles)
		else :
			print form.errors #show errors to user
	else:
		form = PostForm()
	return render_to_response('blog/add_post_simple.html', {'form' : form}, context)

def encode_url(url):
	return url.replace(' ', '_')
