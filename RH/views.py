from django.shortcuts import render
from .models import *
from django.utils import timezone
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import date

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
	return render(request, 'RH/empleados_create.html', {'roles':roles})

def empleados_edit(request,pk):
	empleado=Empleado.objects.get(pk=pk)
	usuario=empleado.usuario
	roles=Rol.objects.all()
	if request.method == "POST":
		empleado=get_object_or_404(Empleado,pk=pk)
		usuario=get_object_or_404(User,pk=empleado.usuario.pk)
		formE=EmpleadoForm(request.POST,instance=empleado)
		formU=UserForm(request.POST,instance=usuario)
		if formU.is_valid() and formE.is_valid():
			formU.save()
			formE.save()
			return HttpResponse('empleado editado')
	return render(request, 'RH/empleados_create.html', {'roles':roles,'empleado':empleado})

def roles_index(request):
	roles=Rol.objects.all()
	return render(request,'RH/roles_index.html',{'roles':roles})

def roles_create(request):
	if request.method == "POST":
		form=RolForm(request.POST)
		if form.is_valid():
			rol=form.save()
			return HttpResponse(rol)
	return render(request,'RH/roles_create.html',{})