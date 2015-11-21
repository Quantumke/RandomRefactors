from django.shortcuts import render_to_response, get_object_or_404
from blogger.models import Post

# Create your views here.

def index(request):
	return render_to_response('index.html',{
		'Post':Post.objects.filter(author='Ben'),
		'cats':Post.objects.filter(group='Grapevine')
               
	})
