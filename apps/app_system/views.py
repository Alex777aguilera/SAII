from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def principal(request):
	ctx = "Hola Mundo"
	
	return render(request,'principal.html',{'mensaje':ctx})

def login_view(request):
    form = LoginForm(request.POST or None)
   
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("principal")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "login.html", {"form": form, "msg": msg})

