from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required
def home(request):
	return render(request,'principal.html')

def ingresar(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/home')
	if request.method == "POST":
	    username = request.POST.get('username')
	    password = request.POST.get('password')
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        # Redirect to a success page.
	        return HttpResponseRedirect('/')
	   
	return render(request, 'sesion/login.html', {})

def salir(request):
	logout(request)
	return HttpResponseRedirect('/login')
