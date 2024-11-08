from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def landing(request):
    if request.user.is_authenticated:
        return redirect("/home")
    return render(request, "landing.html")


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("/login")


@login_required
def home(request):
    options = [
        {"title": "Option 1", "image": "assets/ventura.jpg"},
        {"title": "Option 2", "image": "assets/ventura.jpg"},
        {"title": "Option 3", "image": "assets/ventura.jpg"},
        {"title": "Option 4", "image": "assets/ventura.jpg"},
        {"title": "Option 5", "image": "assets/ventura.jpg"},
        {"title": "Option 6", "image": "assets/ventura.jpg"},
    ]
    return render(request, "home.html", context={"options": options})
