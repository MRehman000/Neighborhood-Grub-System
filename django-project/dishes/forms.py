from django import forms

from dishes.models import Dish, DishRequest, DishPost, OrderFeedback

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
            "meal_time"
        ]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = OrderFeedback
        fields = [
            "feedback",
            "title"
            "tip"
        ]
