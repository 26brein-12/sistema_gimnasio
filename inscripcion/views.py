
from django.shortcuts import render, redirect, get_object_or_404
from .models import Inscripcion
from socios.models import Socio
from clase.models import Clase

def lista_inscripciones(request):
    inscripciones = Inscripcion.objects.all()

    return render(request, 'inscripcion/lista.html', {
        'inscripciones': inscripciones
    })

def crear_inscripcion(request):
    if request.method == 'POST':
        socio_id = request.POST.get('socio')
        clase_id = request.POST.get('clase')

        Inscripcion.objects.create(
            socio_id=socio_id,
            clase_id=clase_id
        )

        return redirect('inscripcion:lista_inscripciones')

    socios = Socio.objects.all()
    clases = Clase.objects.all()

    return render(request, 'inscripcion/crear.html', {
        'socios': socios,
        'clases': clases
    })

def editar_inscripcion(request, id_inscripcion):
    inscripcion = get_object_or_404(
        Inscripcion,
        id_inscripcion=id_inscripcion
    )

    if request.method == 'POST':
        inscripcion.socio_id = request.POST.get('socio')
        inscripcion.clase_id = request.POST.get('clase')
        inscripcion.save()

        return redirect('inscripcion:lista_inscripciones')

    socios = Socio.objects.all()
    clases = Clase.objects.all()

    return render(request, 'inscripcion/editar.html', {
        'inscripcion': inscripcion,
        'socios': socios,
        'clases': clases
    })

def eliminar_inscripcion(request, id_inscripcion):
    inscripcion = get_object_or_404(
        Inscripcion,
        id_inscripcion=id_inscripcion
    )

    if request.method == 'POST':
        inscripcion.delete()
        return redirect('inscripcion:lista_inscripciones')

    return render(request, 'inscripcion/eliminar.html', {
        'inscripcion': inscripcion
    })
