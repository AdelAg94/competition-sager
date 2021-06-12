from django import forms
from .models import Participant, CountryField

class ParticipantForm_F(forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'phone_number':  forms.TextInput(attrs={'class':'form-control'}),
            'country':  forms.Select(attrs={'class':'input'}),
            'skills':  forms.Select(attrs={'class':'form-control'}),
            'photo':  forms.ClearableFileInput(attrs={'class':'form-control input'}),
        }   