from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blogApp.models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogApp/post_detail.html', {'post': post})


class PostListView(ListView):
    model = Post
    template_name = 'blogApp/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogApp/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blogApp/post_new.html'
    fields = {'title', 'body', 'author'}
    # success_url = 'home'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blogApp/post_delete.html'
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blogApp/post_edit.html'
    fields = {'title', 'body'}


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
