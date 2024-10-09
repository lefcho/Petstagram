from django.shortcuts import render, redirect

from Petstagram.pets.forms import AddPetForm, EditPetForm, DeletePetForm
from Petstagram.pets.models import Pet


def add_pet(request):
    form = AddPetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    pet_photos = pet.photos.all()

    context = {
        'pet': pet,
        'pet_photos': pet_photos,
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = EditPetForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('details_pet', 'username', pet.slug)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username ,pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = DeletePetForm(instance=pet)

    if request.method == 'POST':
        pet.delete()

        return redirect('profile-details', pk=1)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-delete-page.html', context)
