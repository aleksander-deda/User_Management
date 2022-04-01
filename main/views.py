from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")        # if we are not logged in, the decorator sends us to login page
def home(request):
    return render(request, 'main/home.html')


@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)   # commit=False bcs we haven't defined the author yet
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()
    
    return render(request, 'main/create_post.html', {'form': form})


def sign_up(request):  
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm
    
    return render(request, 'registration/sign_up.html', {"form": form})


