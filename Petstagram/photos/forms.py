from django import forms

from Petstagram.photos.models import Photo


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class AddPhotoForm(BasePhotoForm):
    pass


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']


class DeletePhotoForm(BasePhotoForm):
    pass