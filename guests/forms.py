from django import forms
from .models import Guest
from django.core.exceptions import ValidationError

class GuestForm(forms.ModelForm):
 
    visit_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Format: YYYY-MM-DD'
    )

    class Meta:
        model = Guest
        fields = ['name', 'visit_date', 'guiders']

    def clean_visit_date(self):
        date = self.cleaned_data.get('visit_date')
        if not date:
            raise ValidationError('Please enter a valid date')
        return date