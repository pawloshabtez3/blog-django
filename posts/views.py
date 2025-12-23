from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, pk):
    post_obj = get_object_or_404(Post, id=pk)
    return render(request, 'posts.html', {'post': post_obj})