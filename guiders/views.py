from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required

from .forms import GuiderForm
from .models import Guider 
from django.contrib import messages

@login_required
def add_guider(request):
    if request.method == 'POST':
        form = GuiderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guider_list')
    else:
        form = GuiderForm()
    return render(request, 'guiders/add_guider.html', {'form': form})


@login_required
def guider_list(request):
    guiders = Guider.objects.all()  
    return render(request, 'guiders/guider_list.html', {'guiders': guiders})


@login_required
def edit_guide(request, guide_id):
    guide = get_object_or_404(Guider, pk=guide_id)
    
    if request.method == "POST":
        form = GuiderForm(request.POST, instance=guide)
        if form.is_valid():
            form.save()
            return redirect('guider_list')  
    else:
        form = GuiderForm(instance=guide)
    
    return render(request, 'guiders/edit_guide.html', {'form': form, 'guide': guide})

@login_required
def delete_guider(request, guide_id):
    guider = get_object_or_404(Guider, pk=guide_id)
    guider.delete()
    messages.success(request, 'Guider deleted successfully!')
    return redirect('guider_list')