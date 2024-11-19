

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import TruncMonth
from animals.models import Animal
from guiders.models import Guider
from guests.models import Guest


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def statistics_view(request):
   
    stats = {
        'total_animals': Animal.objects.count(),
        'total_guiders': Guider.objects.count(),
        'total_guests': Guest.objects.count(),
    }

    species_counts = Animal.objects.values('species').annotate(
        count=Count('id')
    )
    stats['species_labels'] = [item['species'] for item in species_counts]
    stats['species_counts'] = [item['count'] for item in species_counts]
  
    visitor_trends = Guest.objects.annotate(
        month=TruncMonth('visit_date')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')
    
    stats['visitor_months'] = [item['month'].strftime('%B %Y') for item in visitor_trends]
    stats['visitor_counts'] = [item['count'] for item in visitor_trends]
    
    return render(request, 'statistics.html', stats)