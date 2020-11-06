from django import forms
#from django.forms import ModelForm

from .models import *

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
        }
