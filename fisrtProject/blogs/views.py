from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blogs, Comment
from django.contrib import messages
from django.urls import reverse
from . import forms

def handler404(request):
	return render(request, '404.html', status=404)

def index(request):
	blogs = Blogs.objects.all()				   
	return render(request, 'blogs/index.html', {'blogs':blogs})

def single(request, id):
	# blog = Blogs.objects.get(pk = id) # pk adalah primary key
	blog = get_object_or_404(Blogs, pk=id)
	form = forms.CommentForm()
	return render(request, 'blogs/single.html', {'blog':blog, 'form':form})


def comment(request, id):
	blog = get_object_or_404(Blogs, pk=id)
	form = forms.CommentForm()

	if request.method == 'POST':
		form = forms.CommentForm(request.POST)
		if form.is_valid():
			newDesc = request.POST['desc']
			blog.comment_set.create(desc=newDesc)
			messages.success(request, 'Berhasil Submit Komentar')
			return HttpResponseRedirect(reverse('blogs:index'))

	return render(request, 'blogs/single.html', {'blog':blog, 'form':form})

def comment_edit(request, id):
	comment = get_object_or_404(Comment, pk=id)
	form = forms.CommentForm(instance=comment)

	if request.method == 'POST':
		form = forms.CommentForm(instance=comment, data=request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Komentar Berhasil di Update!!')
			return HttpResponseRedirect(reverse('blogs:index'))

	return render(request, 'blogs/comment-edit.html', {'comment':comment, 'form':form})