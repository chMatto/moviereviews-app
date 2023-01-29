from django.shortcuts import render

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError  # database error checker
from .forms import UserCreateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# This help us to create automatic signup form included in Django package
def signupaccount(request):
    if request.method == "GET":
        return render(request, "signupaccount.html", {"form": UserCreateForm})
    else:
        # password1 and password2 is from the 'form' tag.
        if request.POST["password1"] == request.POST["password2"]:
            # This is use to check if the username alredy exits
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "signupaccount.html",
                    {
                        "form": UserCreateForm,
                        "error": "Username already taken, Choose new username.",
                    },
                )

        else:
            return render(
                request,
                "signupaccount.html",
                {"form": UserCreateForm, "error": "Password do not match"},
            )

@login_required
def logoutaccount(request):
    logout(request)
    return redirect("home")


def loginaccount(request):
    if request.method == "GET":
        # The form, will relay the Form to the page loginaccount.html
        return render(request, "loginaccount.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "loginaccount.html",
                {
                    "form": AuthenticationForm(),
                    "error": "username and password do not match",
                },
            )
        else:
            login(request, user)
            return redirect("home")
