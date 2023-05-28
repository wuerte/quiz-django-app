from django import forms
from .models import Question

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(label='Wgraj plik CSV')
