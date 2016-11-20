from django import forms
from accounts.models import CreateAccountRequest

class CreateAccountRequestForm(forms.ModelForm):
    class Meta:
        model = CreateAccountRequest
        fields = ["first_name", "last_name", "email"]

class TerminateAccountRequestForm(forms.Form):
    NO = 0
    YES = 1
    choice = forms.fields.ChoiceField(choices=((YES, "Yes"), (NO, "No")))
