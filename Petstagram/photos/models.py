from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.pets.models import Pet
from Petstagram.photos.validators import MaxFileSizeValidator


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='mediafiles',
        validators=[
            MaxFileSizeValidator(5),
        ],
    )

    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10),
        ],
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
        related_name='tagged_photos',
    )

    date_of_publication = models.DateField(
        auto_now_add=True,
    )