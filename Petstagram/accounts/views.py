from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Petstagram.accounts.forms import AppUserCreationForm

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


def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, 'accounts/profile-delete-page.html')
