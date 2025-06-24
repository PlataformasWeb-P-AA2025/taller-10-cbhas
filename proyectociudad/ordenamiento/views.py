from django.shortcuts import render
from ordenamiento.models import Parroquia, Barrio


def parroquias_barrios(request):
    parroquias = Parroquia.objects.all()
    informacion_template = {
        'parroquias': parroquias,
        'numero_parroquias': parroquias.count(),
    }
    return render(request, 'parroquias_barrios.html', informacion_template)


def barrios(request):
    barrios = Barrio.objects.all()
    informacion_template = {
        'barrios': barrios,
        'numero_barrios': barrios.count(),
    }
    return render(request, 'barrios.html', informacion_template)


def crear_parroquia(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        tipo = request.POST.get('tipo')
        parroquia = Parroquia(nombre=nombre, ubicacion=ubicacion, tipo=tipo)
        parroquia.save()
        return render(request, 'crear_parroquia.html', {'mensaje': 'Parroquia creada exitosamente'})
    return render(request, 'crear_parroquia.html')


def crear_barrio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_viviendas = int(request.POST.get('numero_viviendas'))
        numero_parques = int(request.POST.get('numero_parques'))
        numero_edificios_residenciales = int(request.POST.get('numero_edificios_residenciales'))
        parroquia_id = request.POST.get('parroquia')
        parroquia = Parroquia.objects.get(id=parroquia_id)
        barrio = Barrio(
            nombre=nombre,
            numero_viviendas=numero_viviendas,
            numero_parques=numero_parques,
            numero_edificios_residenciales=numero_edificios_residenciales,
            parroquia=parroquia
        )
        barrio.save()
        return render(request, 'crear_barrio.html', {'mensaje': 'Barrio creado exitosamente'})
    parroquias = Parroquia.objects.all()
    return render(request, 'crear_barrio.html', {'parroquias': parroquias})
