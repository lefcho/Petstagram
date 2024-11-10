
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Petstagram.common.forms import AddCommentForm
from Petstagram.pets.forms import AddPetForm, EditPetForm, DeletePetForm
from Petstagram.pets.models import Pet


class AddPetView(CreateView):
    model = Pet
    template_name = 'pets/pet-add-page.html'
    form_class = AddPetForm

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


class DetailsPetView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_photos'] = self.object.photos.all()
        context['comment_form'] = AddCommentForm()

        return context


class EditPetView(UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    form_class = EditPetForm
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse_lazy(
            'details_pet',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug']
            }
        )


class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    form_class = DeletePetForm
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})
    slug_url_kwarg = 'pet_slug'

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs
