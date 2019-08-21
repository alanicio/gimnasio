from django.contrib import admin
from .models import *
#pass nonex123 user admin
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Responsabilidad)
admin.site.register(Asistencia)
admin.site.register(Permiso)
