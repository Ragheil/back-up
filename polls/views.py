from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


from django.contrib import messages

from .forms import OrderForm, CreateUserForm
from polls.models import Post
from polls.forms import PostForm
from polls.serializers import PostSerializer
# Create your views here.
def register(request):
    form =CreateUserForm()

    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'The account' + " " + user + " " + 'successfully created!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login(request):
    form =UserCreationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def profile(request):
    return render(request, 'profile.html')

class PostListView(ListView):
    template_name = 'home.html'
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'profile.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'register.html'
    success_url = "/post/"

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'EditTask.html'
    context_object_name = 'post'
    success_url = '/post/'

class PostDeleteView(DeleteView):
    template_name = 'taskconfirmdelete.html'
    model = Post
    success_url = '/post/'

class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class= PostSerializer
    queryset = Post.objects.all()
    