from django import forms

from .models import Projecte

class ProjectForm(forms.ModelForm):
    # contact_name = forms.CharField(required=True)
    # contact_email = forms.EmailField(required=True)
    # content = forms.CharField(
    #     required=True,
    #     widget=forms.Textarea
    # )
    
    class Meta:
        model = Projecte
        fields = ['nom','descripcio','presupost','tipus','objectiu','maxim','minim','data_inici','data_fi']