from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, PostForm, UpdateUserForm, UpdateUserProfileForm, RatingsForm
from rest_framework import viewsets
from .models import Profile, Post, Rating
from .serializers import ProfileSerializer, UserSerializer, PostSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import random

@login_required(login_url='login')
def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        posts = Post.objects.all()
        print(posts)
    except Post.DoesNotExist:
        posts = None
    return render(request, 'index.html', {'posts': posts, 'form': form, })
