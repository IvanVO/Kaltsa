from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.phone_number = self.cleaned_data["phone_number"]
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model: Profile
        fields = '__all__'
        exclude = ['user']

class MissingPersonForm(forms.ModelForm):
    class Meta:
        model = MissingPerson
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(
                attrs = {'class':'form-control', 'placeholder':'Nombre completo'}
            ),
            'age': forms.TextInput(
                attrs = {'class':'form-control', 'placeholder':'Edad'}
            ),
            'gender': forms.Select(attrs = {'class':'form-control', 'name':'Género'}
            ),
            'height': forms.TextInput(
                attrs = {'class':'form-control', 'placeholder':'Altura'}
            ),
            'skin_color': forms.Select(
            attrs = {'class':'form-control', 'name':'Color de piel'}
            ),
            'eye_color': forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Color de ojos'}
            ),
            'hair_color': forms.TextInput(
                attrs = {'class':'form-control', 'placeholder':'Color de cabello'}
            ),
            'unique_characteristics': forms.Textarea(attrs = {'class':'form-control', 'cols':2, 'rows':2, 'placeholder':'Vestimenta & características únicas'}
            ),
            'additional_info': forms.Textarea(attrs = {'class':'form-control', 'cols':4, 'rows':4, 'placeholder':'Información adicional'}
            ),
            'contact_full_name': forms.TextInput(
                attrs = {'class':'form-control', 'placeholder':'Nombre de contacto'}
            ),
            'phone_number': forms.TextInput(
                attrs = {'class':'form-control', 'placeholder':'Número de teléfono'}
            ),
            'last_seen_in': forms.TextInput(
                attrs = {'class':'form-control', 'placeholder':'Última vez visto en'}
            ),
            'date_and_time': forms.DateTimeInput(attrs = {'type':'datetime-local', 'class':'form-control'}
            ),
            'state': forms.Select(
            attrs = {'class':'form-control', 'name':'Estado'}
            ),
            'municipio': forms.Select(
            attrs = {'class':'form-control', 'name':'Estado'}
            ),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['municipio'].queryset = Municipio.objects.none()

            if 'state' in self.data:
                try:
                    state_id = int(self.data.get('state'))
                    self.fields['municipio'].queryset = City.objects.filter(state_id=state_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['state'].queryset = self.instance.state.municipio_set.order_by('name')

class giveClueForm(forms.ModelForm):
    class Meta:
        model = Clue
        exclude =['clue_of']

        widgets = {
            'seen_in': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Visto en'}
            ),
            'date_and_time': forms.DateTimeInput(attrs = {'type':'datetime-local', 'class':'form-control'}
            ),
            'state': forms.Select(
            attrs = {'class':'form-control', 'name':'Estado'}
            ),
            'municipio': forms.Select(
            attrs = {'class':'form-control', 'name':'Estado'}
            ),
            'additional_info': forms.Textarea(attrs = {'class':'form-control', 'cols':4, 'rows':4, 'placeholder':'Información adicional'}
            ),
            'phone_number': forms.TextInput(
                attrs = {'class':'form-control', 'placeholder':'Número de teléfono'}
            ),
        }
