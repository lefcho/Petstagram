# Generated by Django 5.1.1 on 2024-09-28 16:04

import Petstagram.photos.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='mediafiles', validators=[Petstagram.photos.validators.MaxFileSizeValidator(5)])),
                ('description', models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_publication', models.DateField(auto_now_add=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, related_name='tagged_photos', to='pets.pet')),
            ],
        ),
    ]