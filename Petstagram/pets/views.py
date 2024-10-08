from django.shortcuts import render

from Petstagram.pets.models import Pet


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    pet_photos = pet.photos.all()

    context = {
        'pet': pet,
        'pet_photos': pet_photos,
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request):
    return render(request, 'pets/pet-edit-page.html')


def delete_pet(request):
    return render(request, 'pets/pet-delete-page.html')
