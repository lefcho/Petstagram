from django.shortcuts import render, redirect

from Petstagram.photos.forms import AddPhotoForm, EditPhotoForm
from Petstagram.photos.models import Photo


def add_photo(request):
    form = AddPhotoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        photo = form.save(commit=False)
        photo.user = request.user
        photo.save()

        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.likes.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = EditPhotoForm(request.POST or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('details_photo', pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')
