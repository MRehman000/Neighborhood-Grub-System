from django import forms
from dishes.models import (
    Dish, DishRequest, DishPost, Chef,
    OrderFeedback, RateChef, RateDiner, Rating
)

# Watson Dependencies
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

# Getting APIKEY variable from settings.py 
APIKEY = getattr(settings, "APIKEY", None)

# Watson authentication
alchemy_language = AlchemyLanguageV1(api_key=APIKEY)

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "name",
            "description"
        ]

class DishRequestForm(forms.ModelForm):
    class Meta:
        model = DishRequest
        fields = [
            "portion_size",
            "num_servings",
            "price",
            "meal_time"
        ]

class DishPostForm(forms.ModelForm):
    class Meta:
        model = DishPost
        fields = [
            "max_servings",
            "serving_size",
            "price",
            "last_call",
            "meal_time",
            "latitude",
            "longitude"
        ]
        widgets = {
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput()
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = OrderFeedback
        fields = [
            "feedback",
            "tip"
        ]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]

class RateChefForm(forms.ModelForm):
    class Meta:
        model = RateChef
        fields =[
            "rating"
        ]

class RateDinerForm(forms.ModelForm):
    class Meta:
        model = RateDiner
        fields =[
            "rating"
        ]

class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = [
            "name",
            "blurb",
            "experience"
        ]

class DishSuggestionForm(forms.ModelForm):
    class Meta:
	model = DishSuggestions
	suggestion = forms.Charfield()

	
	def ask_watson(self):
	    cuisine_tag = self.cleaned_data['suggestion']
	    combined_operations = ['taxonomy']	
	    return alchemy_language.combined(text=cuisine_tag
