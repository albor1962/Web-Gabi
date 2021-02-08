from django.urls import path
from . import views

app_name = 'inicio'
urlpatterns = [
    path('', views.proyectos_list, name='proyectos_list'),
    path('ver_detalles/<int:id>/', views.ver_detalles, name='ver_detalles'),
    path('academico/<int:categoria_id>/', views.academico, name='academico'),
    path('colaboraciones/<int:categoria_id>/', views.colaboraciones, name='colaboraciones'),
    path('profesionales/<int:categoria_id>/', views.profesionales, name='profesionales'),
    path('experiencia-laboral/<int:categoria_id>/', views.exp_laboral, name='exp_laboral'),
    path('publicaciones/<int:categoria_id>/', views.publicaciones, name='publicaciones'),
    path('fotos/', views.fotografia, name='fotos'),
    ]
