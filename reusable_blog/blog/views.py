# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    """create a view that wil return a lost of posts that were published prior to now"""
    posts = Post.objects.filter(published_date__lte=timezone.now()
            ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts':posts})

def post_detail(request,id):
    """
    create a view that returns a single Post object based on the post ID and render it to the 'postdetail.html' template.
    or return a 404 error if the post is not found
    """
    post=get_object_or_404(Post, pk=id)
    post.views+=1  #clock up the number of post views
    post.save()
    return render(request,"blog/postdetail.html",{'post':post})

def top_posts(request):
    """get a list of posts and order them by the number of views. Only return the top 5 results.
    Render it to blogposts.html"""
    posts=Post.objects.filter(published_date__lte= timezone.now()
                              ).order_by('-views')[:5]
    return render(request,"blogposts.html",{'posts':posts})

def new_post(request):
    if request.method=="POST":
        form=BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
        else:
            form = BlogPostForm()
        return render(request, 'blogpostform.html',{'form':form})

def edit_post(request,id):
    post=get_object_or_404(Post, pk=id)
    if request.method=="POST":
        form=BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
        else:
            form=BlogPostForm(instance=post)
        return render(request,'blogpostform.html',{'form':form})
