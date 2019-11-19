from django import forms
from .models import survey, field, CHOICES


example1 = 'example1'
example2 = 'example2'
example3 = 'example3'
example4 = 'example4'

WIDGETS = (
    ('example1', 'example1'),
    ('example2', 'example2'),
    ('example3', 'example3'),
    ('example4', 'example4')
)
# Dummy pre-populated options to fill the widgets
# ------------------------------------------------------------------------------------------------------------

class SurveyForm(forms.ModelForm):
    class Meta:
        model = survey
        fields = '__all__'


class FieldForm(forms.ModelForm):
    class Meta:
        model = field
        fields = '__all__'


class TypeForm(forms.Form):
    text = forms.CharField()
    single = forms.ChoiceField(widget=forms.Select, choices=WIDGETS)
    multiple = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=WIDGETS)
    radio = forms.ChoiceField(widget=forms.RadioSelect, choices=WIDGETS)

        
