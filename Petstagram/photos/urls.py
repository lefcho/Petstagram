from django.urls import path, include
from Petstagram.photos import views

urlpatterns = [
    path('', include([
        path('add/', views.add_photo, name='add_photo'),
        path('<int:pk>/', include([
            path('', views.details_photo, name='details_photo'),
            path('edit/', views.edit_photo, name='edit_photo'),
            path('delete/', views.delete_photo, name='delete_photo'),
        ]))
    ]))
]