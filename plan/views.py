
from django.shortcuts import render, redirect, get_object_or_404
from .models import Plan


def lista_planes(request):
    planes = Plan.objects.all()
    return render(request, 'plan/lista.html', {'planes': planes})


def crear_plan(request):
    if request.method == 'POST':
        nombre_plan = request.POST.get('nombre_plan')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        duracion_dias = request.POST.get('duracion_dias')
        activo = request.POST.get('activo') == 'on'

        Plan.objects.create(
            nombre_plan=nombre_plan,
            descripcion=descripcion,
            precio=precio,
            duracion_dias=duracion_dias,
            activo=activo
        )

        return redirect('plan:lista_planes')

    return render(request, 'plan/crear.html')


def editar_plan(request, id_plan):
    plan = get_object_or_404(Plan, id_plan=id_plan)

    if request.method == 'POST':
        plan.nombre_plan = request.POST.get('nombre_plan')
        plan.descripcion = request.POST.get('descripcion')
        plan.precio = request.POST.get('precio')
        plan.duracion_dias = request.POST.get('duracion_dias')
        plan.activo = request.POST.get('activo') == 'on'

        plan.save()
        return redirect('plan:lista_planes')

    return render(request, 'plan/editar.html', {'plan': plan})


def eliminar_plan(request, id_plan):
    plan = get_object_or_404(Plan, id_plan=id_plan)

    if request.method == 'POST':
        plan.delete()
        return redirect('plan:lista_planes')

    return render(request, 'plan/eliminar.html', {'plan': plan})

