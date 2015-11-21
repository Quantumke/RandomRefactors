from django.shortcuts import render_to_response, get_object_or_404
from blogger.models import Post

# Create your views here.

def index(request):
	return render_to_response('index.html',{
<<<<<<< HEAD
		'Post':Post.objects.filter(author='Ben'),
		'cats':Post.objects.filter(group='Grapevine')
               
=======
		'Post':Post.objects.all()[:5]
>>>>>>> 8bb6879efff4d6b1dd8ec3b3ff5a48ee6000e3f8
	})
