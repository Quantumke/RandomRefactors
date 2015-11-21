from django.shortcuts import render_to_response, get_object_or_404
from blogger.models import Post
from django.db.models import F

# Create your views here.

def index(request):
	return render_to_response('index.html',{

		'Post':Post.objects.filter(author='Ben'),
		'cats':Post.objects.filter(group='Grapevine'),
		'hit':Post.objects.filter(pk=1).update(counter=F('counter') + 1),
	        'popular':Post.objects.order_by('-counter')	
	})
