from django.shortcuts import render
from .models import *
from django.utils import timezone
from .forms import *
from django.http import HttpResponse

# Create your views here.
def empleados_index(request):
	empleados=Empleado.objects.all()
	return render(request,'RH/empleados_index.html',{'empleados':empleados})

def empleados_create(request):
	roles=Rol.objects.all()
	if request.method == "POST":
		formU=UserForm(request.POST)
		formE = EmpleadoForm(request.POST)
		if formU.is_valid() and formE.is_valid():
			user=formU.save()
			empleado=formE.save(commit=False)
			empleado.usuario=user
			empleado.save()
			return HttpResponse('guardado')
		else:
			return HttpResponse(formU.is_valid())
	else:
		form = EmpleadoForm()
	return render(request, 'RH/empleados_create.html', {'roles':roles})

def roles_create(request):
	if request.method == "POST":
		form=RolForm(request.POST)
		if form.is_valid():
			rol=form.save()
			return HttpResponse(rol)
	return render(request,'RH/roles_create.html',{})