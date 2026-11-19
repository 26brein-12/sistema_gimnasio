from django.shortcuts import render, redirect, get_object_or_404
from .models import entrenador


def lista_entrenadores(request):
    entrenadores = entrenador.objects.all()
    return render(request, 'entrenador/lista.html', {
        'entrenadores': entrenadores
    })


def crear_entrenador(request):
    if request.method == 'POST':
        entrenador.objects.create(
            documento=request.POST.get('documento'),
            nombre=request.POST.get('nombre'),
            telefono=request.POST.get('telefono'),
            especialidad=request.POST.get('especialidad'),
            activo=request.POST.get('activo') == 'on'
        )
        return redirect('entrenador:lista_entrenadores')

    return render(request, 'entrenador/crear.html')


def editar_entrenador(request, id_entrenador):
    profesor = get_object_or_404(
        entrenador, id_entrenador=id_entrenador
    )

    if request.method == 'POST':
        profesor.documento = request.POST.get('documento')
        profesor.nombre = request.POST.get('nombre')
        profesor.telefono = request.POST.get('telefono')
        profesor.especialidad = request.POST.get('especialidad')
        profesor.activo = request.POST.get('activo') == 'on'
        profesor.save()

        return redirect('entrenador:lista_entrenadores')

    return render(request, 'entrenador/editar.html', {
        'entrenador': profesor
    })


def eliminar_entrenador(request, id_entrenador):
    profesor = get_object_or_404(
        entrenador, id_entrenador=id_entrenador
    )

    if request.method == 'POST':
        profesor.delete()
        return redirect('entrenador:lista_entrenadores')

    return render(request, 'entrenador/eliminar.html', {
        'entrenador': profesor
    })

