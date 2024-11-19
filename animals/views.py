from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AnimalForm  
from .models import Animal  
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


@login_required

def add_animals(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')  
    else:
        form = AnimalForm()
    return render(request, 'animals/add_animal.html', {'form': form})


@login_required
def animal_list(request):
    animals = Animal.objects.all()  
    return render(request, 'animals/animal_list.html', {'animals': animals})


@login_required
def edit_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Animal updated successfully!')
            return redirect('animal_list')
    else:
        form = AnimalForm(instance=animal)
    
    return render(request, 'animals/edit_animal.html', {'form': form, 'animal': animal})

@login_required
def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    animal.delete()
    messages.success(request, 'Animal deleted successfully!')
    return redirect('animal_list')


