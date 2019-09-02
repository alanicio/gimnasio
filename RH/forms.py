from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('username','password','email')

class EmpleadoForm(forms.ModelForm):
	class Meta:
		model=Empleado
		fields=(
			'nombre',
			'apellido_paterno',
			'apellido_materno',
			'fecha_de_nacimiento',
			'rol',
			)

class RolForm(forms.ModelForm):
	class Meta:
		model=Rol
		fields=('nombre','descripcion')

class ResponsabilidadForm(forms.ModelForm):
	roles=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Rol.objects.all(),required=False)
	empleados=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Empleado.objects.all(),required=False)
	class Meta:
		model=Responsabilidad
		fields=(
			'nombre',
			'descripcion',
			'empleados',
			'roles',
			)