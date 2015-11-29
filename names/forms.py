from django import forms
from names.models import Name

class NameForm(forms.ModelForm):
    
    class Meta:
        model = Name
        fields = ['name', 'used',]
        widgets = {
            'name': forms.TextInput(attrs={"autofocus": True, "autocorrect": "off", "autocapitalize": "off"}),
        }
