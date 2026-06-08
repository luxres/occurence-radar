from django import forms
from .models import OccurrenceModel

class ReportForm(forms.ModelForm):
    class Meta:
        model = OccurrenceModel
        fields = ['event_type', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }