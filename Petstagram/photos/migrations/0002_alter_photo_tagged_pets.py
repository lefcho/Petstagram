# Generated by Django 5.1.1 on 2024-10-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, related_name='photos', to='pets.pet'),
        ),
    ]
