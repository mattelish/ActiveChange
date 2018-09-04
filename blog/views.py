from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.decorators import login_required
from.import forms


# Create your views here.

def blog_list(request):
	blog = Blog.objects.all().order_by('date')
	return render(request, 'blog/blog_list.html', {'blog': blog})


def blog_detail(request, slug):
	#return HttpResponse(slug)
	blog = Blog.objects.get(slug=slug)
	return render(request, 'blog/blog_detail.html', {'blog': blog})

@login_required(login_url="/accounts/login/")
def blog_create(request):
  if request.method == 'POST':
     form = forms.CreateBlog(request.POST,request.FILES)
     if form.is_valid():
       	#save blog to db
       	instance = form.save(commit=False)
       	instance.author = request.user
       	instance.save()
       	return redirect('blog:list')
  else:
	  form = forms.CreateBlog()
  return render(request, 'blog/blog_create.html', { 'form': form })