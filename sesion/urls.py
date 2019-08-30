from django.urls import path
from . import views

urlpatterns=[
	path('login',views.ingresar,name='ingresar'),
	path('salir',views.salir,name='salir'),
	path('',views.home,name='home'),
]