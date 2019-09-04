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
import sweetify
from django.http import JsonResponse

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
			sweetify.success(request,'Empleado agregado',timer=1500)
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
			sweetify.success(request,'Empleado modificado',timer=1500)
			return empleados_index(request)
	return render(request, 'RH/empleados_create.html', {'roles':roles,'empleado':empleado})

@login_required
def	empleados_delete(request,pk):
	User.objects.filter(pk=Empleado.objects.get(pk=pk).usuario.pk).delete()
	sweetify.success(request,'Empleado eliminado',timer=1500)
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
			sweetify.success(request,'Rol agregado',timer=1500)
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
			sweetify.success(request,'Rol modificado',timer=1500)
			return roles_index(request)
	return render(request,'RH/roles_create.html',{'rol':rol})

@login_required
def roles_delete(request,pk):
	Rol.objects.filter(pk=pk).delete()
	sweetify.success(request,'Rol eliminado',timer=1500)
	return roles_index(request)

@login_required
def responsabilidades_create(request):
	roles=Rol.objects.all()
	empleados=Empleado.objects.all()
	if request.method=="POST":
		form=ResponsabilidadForm(request.POST)
		if form.is_valid():
			form.save()
			sweetify.success(request,'Responsabilidad agregada',timer=1500)
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
			sweetify.success(request,'Responsabilidad modificada',timer=1500)
			return responsabilidades_index(request)
	return render(request,'RH/responsabilidades_create.html',{'roles':roles,'empleados':empleados,'responsabilidad':r})

@login_required
def responsabilidades_delete(request,pk):
	Responsabilidad.objects.filter(pk=pk).delete()
	sweetify.success(request,'Responsabilidad eliminada',timer=1500)
	return responsabilidades_index(request)

@login_required
def asistencias_create(request):
	return render(request,'RH/asistencias_create.html',{})

@login_required
def asistencias_check(request):
	asis=Asistencia.objects.create(tipo='e',empleado=request.user.empleado)
	user=request.user.empleado.nombre+' '+request.user.empleado.apellido_materno
	return JsonResponse({'user':user,'fecha':asis.fecha.strftime('%H:%M')})

@login_required
def asistencias_index(request):
	pass
