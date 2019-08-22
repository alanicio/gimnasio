from django.urls import path
from . import views

urlpatterns=[
	path('',views.empleados_index,name='empleados_index'),
	path('create',views.empleados_create,name='empleados_create'),
	path('roles/create',views.roles_create,name='roles_create'),
]