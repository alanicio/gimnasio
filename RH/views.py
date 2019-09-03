from django.shortcuts import render
from .models import *
from django.utils import timezone
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def empleados_index(request):
	empleados=Empleado.objects.all()
	return render(request,'RH/empleados_index.html',{'empleados':empleados})

@login_required
def empleados_create(request):
	roles=Rol.objects.all()
	if request.method == "POST":
		formU=UserForm(request.POST)
		formE = EmpleadoForm(request.POST)
		# return HttpResponse(formU)
		if formU.is_valid() and formE.is_valid():
			user = User.objects.create_user(username=request.POST.get('username'),
											email=request.POST.get('email'),
											password=request.POST.get('password'))
			empleado=formE.save(commit=False)
			empleado.usuario=user
			empleado.save()
			return empleados_index(request)
	return render(request, 'RH/empleados_create.html', {'roles':roles})

@login_required
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
			usuario.set_password(request.POST.get('password'))
			usuario.save()
			formE.save()
			return empleados_index(request)
	return render(request, 'RH/empleados_create.html', {'roles':roles,'empleado':empleado})

@login_required
def	empleados_delete(request,pk):
	User.objects.filter(pk=Empleado.objects.get(pk=pk).usuario.pk).delete()
	return empleados_index(request)

@login_required
def empleados_show(request,pk):
	empleado=Empleado.objects.get(pk=pk)
	return render(request,'RH/empleados_create.html',{'empleado':empleado,'show':True})


@login_required
def roles_index(request):
	roles=Rol.objects.all()
	return render(request,'RH/roles_index.html',{'roles':roles})

@login_required
def roles_create(request):
	if request.method == "POST":
		form=RolForm(request.POST)
		if form.is_valid():
			rol=form.save()
			return roles_index(request)
	return render(request,'RH/roles_create.html',{})

@login_required
def roles_edit(request,pk):
	rol=Rol.objects.get(pk=pk)
	if request.method=="POST":
		rol=get_object_or_404(Rol,pk=pk)
		form=RolForm(request.POST,instance=rol)
		if form.is_valid():
			form.save()
			return roles_index(request)
	return render(request,'RH/roles_create.html',{'rol':rol})

@login_required
def roles_delete(request,pk):
	Rol.objects.filter(pk=pk).delete()
	return roles_index(request)

@login_required
def responsabilidades_create(request):
	roles=Rol.objects.all()
	empleados=Empleado.objects.all()
	if request.method=="POST":
		form=ResponsabilidadForm(request.POST)
		if form.is_valid():
			form.save()
			return responsabilidades_index(request)
	return render(request,'RH/responsabilidades_create.html',{'roles':roles,'empleados':empleados})

@login_required
def responsabilidades_index(request):
	responsabilidades=Responsabilidad.objects.all()
	return render(request,'RH/responsabilidades_index.html',{'responsabilidades':responsabilidades})

@login_required
def responsabilidades_edit(request,pk):
	r=Responsabilidad.objects.get(pk=pk)
	empleados=Empleado.objects.all()
	roles=Rol.objects.all()
	if request.method=="POST":
		r=get_object_or_404(Responsabilidad,pk=pk)
		form=ResponsabilidadForm(request.POST,instance=r)
		if form.is_valid():
			form.save()
			return responsabilidades_index(request)
	return render(request,'RH/responsabilidades_create.html',{'roles':roles,'empleados':empleados,'responsabilidad':r})

@login_required
def responsabilidades_delete(request,pk):
	Responsabilidad.objects.filter(pk=pk).delete()
	return responsabilidades_index(request)
