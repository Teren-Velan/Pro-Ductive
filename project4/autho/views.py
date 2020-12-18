from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import CreateUserForm
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
# reads of the form.py


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard:index'))

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            login(request, user)

            return HttpResponseRedirect(reverse('dashboard:index'))
        else:
            return render(request, "autho/signup.html", {"form": form})

    form = CreateUserForm()
    return render(request, "autho/signup.html", {"form": form})


def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("dashboard:index"))

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # check if user exist by authenticating user
        # User.objects.get(username=username)
        # if user then check if password == password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard:index"))
        else:
            form = AuthenticationForm(request.POST)
            return render(request, "autho/signin.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, "autho/signin.html", {"form": form})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('autho:signin'))
