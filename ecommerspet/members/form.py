from django import forms
from .models import Participant


class Participantform(forms.ModelForm):
    class meta:
        model = Participant
        feilds = ['name','email','age','phone','paymentmode']