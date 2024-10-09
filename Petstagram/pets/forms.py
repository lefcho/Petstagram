from django import forms

from Petstagram.pets.models import Pet


class BasePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link to image'})
        }
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to image',
        }


class AddPetForm(BasePetForm):
    pass


class EditPetForm(BasePetForm):
    pass


class DeletePetForm(BasePetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
