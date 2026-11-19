from django.shortcuts import render, redirect, get_object_or_404
from .models import Clase
from apps.entrenador.models import entrenador


def lista_clases(request):
    clases = Clase.objects.all()
    return render(request, 'clase/lista.html', {
        'clases': clases
    })


def crear_clase(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        horario = request.POST.get('horario')
        cupo = request.POST.get('cupo')
        entrenador_id = request.POST.get('entrenador')

        Clase.objects.create(
            nombre=nombre,
            horario=horario,
            cupo=cupo,
            entrenador_id=entrenador_id
        )

        return redirect('clase:lista_clases')

    entrenadores = entrenador.objects.all()

    return render(request, 'clase/crear.html', {
        'entrenadores': entrenadores
    })


def editar_clase(request, id_clase):
    clase = get_object_or_404(Clase, id_clase=id_clase)

    if request.method == 'POST':
        clase.nombre = request.POST.get('nombre')
        clase.horario = request.POST.get('horario')
        clase.cupo = request.POST.get('cupo')
        clase.entrenador_id = request.POST.get('entrenador')

        clase.save()
        return redirect('clase:lista_clases')

    entrenadores = entrenador.objects.all()

    return render(request, 'clase/editar.html', {
        'clase': clase,
        'entrenadores': entrenadores
    })

def eliminar_clase(request, id_clase):
    clase = get_object_or_404(Clase, id_clase=id_clase)

    if request.method == 'POST':
        clase.delete()
        return redirect('clase:lista_clases')

    return render(request, 'clase/eliminar.html', {
        'clase': clase
    })
