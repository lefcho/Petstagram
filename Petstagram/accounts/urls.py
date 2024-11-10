from django.contrib.auth.views import LogoutView
from django.urls import path, include
from Petstagram.accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('path/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.AppUserDetailsView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', views.AppUserDeleteView.as_view(), name='profile-delete'),
    ])),
]
