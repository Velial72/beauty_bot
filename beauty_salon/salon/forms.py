from django import forms

from .models import Clients, Salon, Master


class ClientsForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = (
            'td_id',
            'name',
            'client_phone_number'
        )
        widgets = {
            'td_id': forms.TextInput,
            'name': forms.TextInput,
            'client_phone_number': forms.TextInput
        }


class SalonForm(forms.ModelForm):

    class Meta:
        model = Salon
        fields = (
            'id',
            'name',
            'adress'
        )
        widgets = {
            'id': forms.TextInput,
            'name': forms.TextInput,
            'adress': forms.TextInput
        }


class MasterForm(forms.ModelForm):

    class Meta:
        model = Master
        fields = (
            'id',
            'name',
            'working_hours'
        )
        widgets = {
            'id': forms.TextInput,
            'name': forms.TextInput,
            'working_hours': forms.TextInput
        }