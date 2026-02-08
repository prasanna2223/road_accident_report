# accidents/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Accident
from django.contrib.auth.decorators import login_required

@login_required
def accident_list(request):
    if request.user.is_staff:
        accidents = Accident.objects.all()
    else:
        accidents = Accident.objects.filter(user=request.user)
    return render(request, 'accidents/acci_list.html', {'accidents': accidents})

@login_required
def accident_create(request):
    if request.method == "POST":
        Accident.objects.create(
            user=request.user if request.user.is_authenticated else None,
            reporter_name=request.POST.get('reporter_name'),
            phone_number=request.POST.get('phone_number'),
            location=request.POST.get('location'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            accident_date=request.POST.get('accident_date') or None,
            accident_time=request.POST.get('accident_time') or None,
            vehicle_type=request.POST.get('vehicle_type'),
            severity=request.POST.get('severity'),
            description=request.POST.get('description'),
            )
        return redirect('acci_list')

    return render(request, 'accidents/acci_form.html')

def accident_update(request, id):
    accident = get_object_or_404(Accident, id=id)

    if not request.user.is_staff and accident.user != request.user:
        return redirect('acci_list')

    if request.method == "POST":
        accident.reporter_name = request.POST.get('reporter_name')
        accident.phone_number = request.POST.get('phone_number')
        accident.location = request.POST.get('location')
        accident.city = request.POST.get('city')
        accident.state = request.POST.get('state')
        accident.accident_date = request.POST.get('accident_date') or None
        accident.accident_time = request.POST.get('accident_time') or None
        accident.vehicle_type = request.POST.get('vehicle_type')
        accident.severity = request.POST.get('severity')
        accident.description = request.POST.get('description')

        if request.user.is_staff:
            accident.status = request.POST.get('status')

        accident.save()

        return redirect('acci_list')

    return render(request, 'accidents/acci_form.html', {
        'accident': accident
    })

def accident_delete(request, id):
    accident = get_object_or_404(Accident, id=id)

    if request.method == 'POST':
        accident.delete()
        return redirect('acci_list')

    return render(request, 'accidents/acci_delete.html', {
        'accident': accident
    })
