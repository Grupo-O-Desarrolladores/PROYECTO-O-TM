from django import forms
from django.forms import ModelForm
from aplicaciones.donaciones.models import Donacion

class FormaDonacion(forms.Form):
	donante = forms.CharField(max_length=60,widget=forms.TextInput
        (attrs={
            "class": "form-control",
            "placeholder": "Nombre interesado/a"}
        ))
        
	contacto = forms.CharField(max_length=60,widget=forms.TextInput(
		attrs={
			"class": "form-control",
			"placeholder": "Telefono o Mail"
		})
	)