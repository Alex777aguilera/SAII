from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,JsonResponse, HttpResponse
from .forms import LoginForm, SignUpForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from .models import * #Modelos de nuestra aplicacion

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
                msg = 'credentials Invalids '
        else:
            msg = 'Error en validar el formulario'

    return render(request, "login.html", {"form": form, "msg": msg})

@login_required
def cerrar_secion(request):
    logout(request)
    return HttpResponseRedirect(reverse(login_view))



def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Usuario creado - porfavor  <a href="/">Inicio de session</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Datos no validos'
    else:
        form = SignUpForm()
    
    return render(request, "register_user.html", {"form": form, "msg": msg, "success": success})

@login_required
def user_(request):
    user = User.objects.all()
    ctx = {'users':user}
    
    return render(request,'user_.html',ctx)

@login_required
def colaboradores(request):
   
    
    return render(request,'colaboradores.html')


@login_required
def develops(request):
   desarrolladores = Desarrolladores.objects.all()
   cant_int = desarrolladores.__len__()
   
   ctx = {'devs':desarrolladores, 'cantidadD':cant_int}
   
   return render(request,'develops.html',ctx)

@login_required
def calculos(request):
    Pdolar = 24.55
    calculo  = 0.0
   
    if request.method=='POST':
        Cdolar = float(request.POST.get('dinero')) 
    
        calculo  = Cdolar * Pdolar
        print(calculo)
   
    ctx = {'calculo':calculo}
    return render(request,'calculos.html',ctx)