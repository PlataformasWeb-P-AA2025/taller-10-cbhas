from django.contrib import admin
from django.urls import path
from ordenamiento import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.parroquias_barrios, name='parroquias_barrios'),
    path('barrios/', views.barrios, name='barrios'),
    path('crear_parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('crear_barrio/', views.crear_barrio, name='crear_barrio'),

]
