from django.shortcuts import render, redirect
from .models import Membresia
from apps.socios.models import Socio
from apps.plan.models import Plan


def lista_membresias(request):
    membresias = Membresia.objects.all()
    return render(request, 'membresias/lista.html', {
        'membresias': membresias
    })


def crear_membresia(request):
    if request.method == 'POST':
        socio_id = request.POST.get('socio')
        plan_id = request.POST.get('plan')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        Membresia.objects.create(
            socio_id=socio_id,
            plan_id=plan_id,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )

        return redirect('membresias:lista_membresias')

    socios = Socio.objects.all()
    planes = Plan.objects.filter(activo=True)

    return render(request, 'membresias/crear.html', {
        'socios': socios,
        'planes': planes
    })

def editar_membresia(request, id_membresia):
    membresia = Membresia.objects.get(id_membresia=id_membresia)

    if request.method == 'POST':
        membresia.socio_id = request.POST.get('socio')
        membresia.plan_id = request.POST.get('plan')
        membresia.fecha_inicio = request.POST.get('fecha_inicio')
        membresia.fecha_fin = request.POST.get('fecha_fin')
        membresia.save()

        return redirect('membresias:lista_membresias')

    socios = Socio.objects.all()
    planes = Plan.objects.filter(activo=True)

    return render(request, 'membresias/editar.html', {
        'membresia': membresia,
        'socios': socios,
        'planes': planes
    })

def eliminar_membresia(request, id_membresia):
    membresia = Membresia.objects.get(id_membresia=id_membresia)

    if request.method == 'POST':
        membresia.delete()
        return redirect('membresias:lista_membresias')

    return render(request, 'membresias/eliminar.html', {
        'membresia': membresia
    })

