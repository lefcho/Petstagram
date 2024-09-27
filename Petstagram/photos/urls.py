from django.urls import path, include
from Petstagram.photos import views

urlpatterns = [
    path('', include([
        path('add/', views.add_photo, name='add_photo'),
        path('<int:pk>/', views.details_photo, name='details_photo'),
        path('<int:pk>/edit/', views.edit_photo, name='edit_photo'),
    ]))
]