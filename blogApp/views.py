from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blogApp.models import Post


# Create your views here.
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogApp/post_detail.html', {'post': post})


def home(request):
    posts = Post.objects.all()
    return render(request, 'blogApp/home.html', {
        'posts': posts
    })


def hello():
    return HttpResponse('<h1>Cohort 13</h1>')


def greet():
    return HttpResponse('Welcome to django')


def simi(request):
    return render(request, 'blogApp/simex.html')
