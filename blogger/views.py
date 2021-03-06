from django.shortcuts import render_to_response, get_object_or_404
from blogger.models import Post
from django.db.models import F

# Create your views here.

def index(request):
	return render_to_response('index.html',{

		'Post':Post.objects.filter(author='Ben'),
		'cats':Post.objects.filter(group='Grapevine'),
		'hit':Post.objects.filter(pk=1).update(counter=F('counter') + 1),
	        'popular':Post.objects.order_by('-counter'),
		'grapevine':Post.objects.filter(group='Grapevine'),
		'sport':Post.objects.filter(group='Sports'),
		'health':Post.objects.filter(group='Health'),
		'fhealth':Post.objects.filter(group='Health').filter(status='Featured'),
		'lifestyle':Post.objects.filter(group='Lifestyle'),
		'flifestyle':Post.objects.filter(status='Featured').filter(group='Lifestyle'),
		'politics':Post.objects.filter(group='politics'),
		'ppolitcs':Post.objects.filter(group='politics').filter(status='Featured')
	})
