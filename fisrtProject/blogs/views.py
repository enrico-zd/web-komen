from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blogs

def handler404(request):
	return render(request, '404.html', status=404)

def index(request):
	blogs = Blogs.objects.all()				   
	return render(request, 'blogs/index.html', {'blogs':blogs})

def single(request, id):
	# blog = Blogs.objects.get(pk = id) # pk adalah primary key
	blog = get_object_or_404(Blogs, pk=id)
	return render(request, 'blogs/single.html', {'blog':blog})


def comment(request, id):
	blog = get_object_or_404(Blogs, pk=id)

	if request.method == 'POST':
		newDesc = request.POST['komen']

		# cek kalau komentar lebih dari 10 akan error
		if len(newDesc) < 10:
			return render(request, 'blogs/single.html', {
						'blog':blog,
						'errors':'Komentar harus lebih dari sepuluh!!', 
				})	

		blog.comment_set.create(desc=newDesc)
	
	return HttpResponseRedirect('/blogs/' + str(id))