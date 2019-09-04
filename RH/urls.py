from django.urls import path
from . import views

urlpatterns=[
	path('',views.empleados_index,name='empleados_index'),
	path('create',views.empleados_create,name='empleados_create'),
	path('edit/<int:pk>/',views.empleados_edit,name='empleados_edit'),
	path('delete/<int:pk>/',views.empleados_delete,name='empleados_delete'),
	path('<int:pk>/',views.empleados_show,name='empleados_show'),
	path('roles/create',views.roles_create,name='roles_create'),
	path('roles',views.roles_index,name='roles_index'),
	path('roles/edit/<int:pk>/',views.roles_edit,name='roles_edit'),
	path('roles/delete/<int:pk>/',views.roles_delete,name='roles_delete'),
	path('responsabilidades',views.responsabilidades_index,name='r_index'),
	path('responsabilidades/create',views.responsabilidades_create,name='r_create'),
	path('responsabilidades/edit/<int:pk>',views.responsabilidades_edit,name='r_edit'),
	path('responsabilidades/delete/<int:pk>',views.responsabilidades_delete,name='r_delete'),
	path('asistencias/create',views.asistencias_create,name='asis_create'),
	path('asis/checked',views.asistencias_check,name='check'),
	path('asistencias',views.asistencias_index,name='asis_index'),
]