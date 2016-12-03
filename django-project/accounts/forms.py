from django import forms
from accounts.models import CreateAccountRequest, ChefPermissionsRequest
from accounts.models import Suggestion
from captcha.fields import CaptchaField

class CreateAccountRequestForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = CreateAccountRequest
        fields = ["username", "first_name", "last_name", "email"]

class TerminateAccountRequestForm(forms.Form):
    NO = 0
    YES = 1
    choice = forms.fields.ChoiceField(choices=((YES, "Yes"), (NO, "No")))

class ChefPermissionsRequestForm(forms.ModelForm):
    class Meta:
        model = ChefPermissionsRequest
        fields = [
            "first_dish_name",
            "first_dish_image",
            "second_dish_name",
            "second_dish_image",
            "third_dish_name",
            "third_dish_image",
            "video_biography"
        ]

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ["suggestion"]
