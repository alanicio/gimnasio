from django.urls import path
from . import views

urlpatterns=[
	path('',views.empleados_index,name='empleados_index'),
	path('create',views.empleados_create,name='empleados_create'),
	path('edit/<int:pk>/',views.empleados_edit,name='empleados_edit'),
	path('roles/create',views.roles_create,name='roles_create'),
	path('roles',views.roles_index,name='roles_index'),
]