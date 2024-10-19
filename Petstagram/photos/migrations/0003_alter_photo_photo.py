# Generated by Django 5.1.1 on 2024-10-09 18:09

import Petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_tagged_pets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images', validators=[Petstagram.photos.validators.MaxFileSizeValidator(5)]),
        ),
    ]