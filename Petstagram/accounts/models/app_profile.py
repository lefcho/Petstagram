from django.contrib.auth import get_user_model
from django.db import models
UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    