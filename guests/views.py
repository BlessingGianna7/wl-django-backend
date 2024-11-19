from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import GuestForm
from .models import Guest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

@login_required
def add_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guest added successfully!')
            return redirect('guest_list')
        else:
            messages.error(request, 'Error adding guest.')
    else:
        form = GuestForm()
    return render(request, 'guests/add_guest.html', {'form': form})


@login_required
def guest_list(request):
    guests = Guest.objects.all()  
    return render(request, 'guests/guest_list.html', {'guests': guests})


@login_required
def edit_guest(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id) 
    
    if request.method == "POST":
        form = GuestForm(request.POST, instance=guest)  
        if form.is_valid():
            form.save()
            return redirect('guest_list')  
    else:
        form = GuestForm(instance=guest)
    
    return render(request, 'guests/edit_guest.html', {'form': form, 'guest': guest})  

@login_required
def delete_guest(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    guest.delete()
    messages.success(request, 'Guest deleted successfully!')
    return redirect('guest_list')