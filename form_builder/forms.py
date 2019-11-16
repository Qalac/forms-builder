from django import forms
from .models import survey, field

class SurveyForm(forms.ModelForm):
    class Meta:
        model = survey
        fields = '__all__'


class FieldForm(forms.ModelForm):
    class Meta:
        model = field
        fields = '__all__'

        
