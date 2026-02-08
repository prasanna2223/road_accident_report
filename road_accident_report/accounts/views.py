from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from accidents.models import Accident

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('acci_list')
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@staff_member_required
def admin_dashboard(request):
    total_accidents = Accident.objects.count()
    pending_accidents = Accident.objects.filter(status='Pending').count()
    resolved_accidents = Accident.objects.filter(status='Resolved').count()

    severe_count = Accident.objects.filter(severity='High').count()
    medium_count = Accident.objects.filter(severity='Medium').count()
    low_count = Accident.objects.filter(severity='Low').count()

    recent_accidents = Accident.objects.order_by('-accident_date')[:5]

    context = {
        'total_accidents': total_accidents,
        'pending_accidents': pending_accidents,
        'resolved_accidents': resolved_accidents,
        'severe_count': severe_count,
        'medium_count': medium_count,
        'low_count': low_count,
        'recent_accidents': recent_accidents,
    }

    return render(request, 'accounts/admin_dashboard.html', context)

# 👤 USER LOGIN
def user_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # ❌ block admin from user login page
            if user.is_staff:
                return render(request, 'accounts/user_login.html', {
                    'form': form,
                    'error': 'Admins must use admin login'
                })

            login(request, user)
            return redirect('acci_list')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/user_login.html', {'form': form})


# 🛡️ ADMIN LOGIN
def admin_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # ❌ block normal users
            if not user.is_staff:
                return render(request, 'accounts/admin_login.html', {
                    'form': form,
                    'error': 'You are not an admin'
                })

            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/admin_login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('user_login')
