from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from Petstagram.accounts.forms import AppUserCreationForm, ProfileEditForm

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    template_name = 'accounts/register-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
    form_class = AppUserCreationForm

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class AppUserLoginView(LoginView):
    template_name = 'accounts/login-page.html'


class AppUserDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_likes_count'] = sum(p.likes.count() for p in self.object.photos.all())

        return context


class ProfileEditView(UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    form_class = ProfileEditForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )


def delete_profile(request):
    return render(request, 'accounts/profile-delete-page.html')
