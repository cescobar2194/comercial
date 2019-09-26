from django import forms
from .models import Publicacion

class PubForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ('titulo', 'texto',)
