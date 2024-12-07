from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import Group


TEACHER_GROUP_NAME = 'teacher'


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "account/register.html", {"form": form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            print(user)
            if form.cleaned_data['role'] == 'Teacher':
                group = Group.objects.get(name=TEACHER_GROUP_NAME)
                user.is_staff = True
                user.groups.add(group)
                user.save()
            # user.save()
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return redirect(reverse("home"))
        else:
            return render(request, "account/register.html", {"form": form})


def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, f"Invalid username or password")
        return render(request, "account/login.html", {"form": form})


def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
