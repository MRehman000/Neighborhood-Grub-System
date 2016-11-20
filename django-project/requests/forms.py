from django import forms
from requests.models import CreateAccountRequest

class CreateAccountRequestForm(forms.ModelForm):
    class Meta:
        model = CreateAccountRequest
        fields = ["first_name", "last_name", "email"]
