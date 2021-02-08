from django.shortcuts import render
from .models import Proyecto,Imagen,Fofografia


def proyectos_list(request):
    proyectos = Proyecto.objects.filter(estado=True)
    return render(request, 'inicio/proyectos.html', {'proyectos': proyectos})

def ver_detalles(request, id):
    detalles = Imagen.objects.filter(proyecto=id)
    contexto = {
        'detalles':detalles,
    }
    return render(request, 'inicio/galeria.html', contexto)

def academico(request, categoria_id):
    academicos = Proyecto.objects.filter(categoria_id=2)
    contexto = {'academicos':academicos}
    return render(request, 'inicio/academico.html', contexto)

def colaboraciones(request, categoria_id):
    colaboraciones = Proyecto.objects.filter(categoria_id=1)
    return render(request, 'inicio/colaboraciones.html', {'colaboraciones':colaboraciones})

def profesionales(request, categoria_id):
    profesionales = Proyecto.objects.filter(categoria_id=3)
    return render(request, 'inicio/profesionales.html', {'profesionales':profesionales})

def exp_laboral(request, categoria_id):
    laborales = Proyecto.objects.filter(categoria_id=4)
    return render(request, 'inicio/exp_laboral.html', {'laborales':laborales})

def publicaciones(request, categoria_id):
    publicaciones = Proyecto.objects.filter(categoria_id=5)
    return render(request, 'inicio/publicaciones.html', {'publicaciones':publicaciones})

def fotografia(request):
    fotos = Fofografia.objects.filter(estado=True)
    return render(request, 'inicio/fotografia.html', {'fotos':fotos})