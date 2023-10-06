from audioop import reverse
import imp
from msilib.schema import ListView
from re import template
from attr import fields
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegisterUserForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from accounts.models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy

# Create your views here.
def indexView(request):
    return render(request,'index.html')

def dashboardView(request):
    return render(request,'dashboard.html')

class HomeView(ListView):
    model = Post
    template_name = 'post_page.html'
    ordering = ['post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    #fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_page')

def profileView(request):
    return render(request,'profile.html')

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
        else:
            messages.success(request,("Warning! There was an error login. Try again!"))
            return redirect('login_user')

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,("You have logged out! Bye!"))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("Registered good"))
            return redirect('dashboard')
    else:
        form = RegisterUserForm()  
    return render(request, 'authenticate/register.html', {'form':form,})
