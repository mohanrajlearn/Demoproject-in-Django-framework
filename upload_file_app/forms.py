# myapp/forms.py
from django import forms
from .models import UploadedData

class UploadedDataForm(forms.ModelForm):
    class Meta:
        model = UploadedData
        fields = ['file']
