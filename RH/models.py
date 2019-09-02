from django.db import models
from django.utils import timezone

# Create your models here.
class Rol(models.Model):
	nombre=models.CharField(max_length=120)
	descripcion=models.TextField()
	#Agregar modulos y/o submodulos booleanos

class Empleado(models.Model):
	nombre=models.CharField(max_length=120)
	apellido_paterno=models.CharField(max_length=120)
	apellido_materno=models.CharField(max_length=120,blank=True,null=True)
	fecha_de_nacimiento=models.DateTimeField(blank=True,null=True)
	fecha_de_alta=models.DateTimeField(default=timezone.now)
	rol=models.ForeignKey(Rol,on_delete=models.CASCADE)
	usuario=models.ForeignKey('auth.User',on_delete=models.CASCADE)

class Responsabilidad(models.Model):
	nombre=models.CharField(max_length=120)
	descripcion=models.TextField()
	empleados=models.ManyToManyField(Empleado,blank=True)
	roles=models.ManyToManyField(Rol,blank=True)

class Asistencia(models.Model):
	fecha=models.DateTimeField(default=timezone.now)
	tipo=models.CharField(max_length=1)
	empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)

class Permiso(models.Model):
	descripcion=models.TextField()
	motivo=models.TextField()
	created_at=models.DateTimeField(default=timezone.now)
	fecha_de_permiso=models.DateTimeField()
	empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)





