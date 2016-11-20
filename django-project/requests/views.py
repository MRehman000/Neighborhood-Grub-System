from django.shortcuts import get_object_or_404, render, redirect

from requests.forms import CreateAccountRequestForm
from requests.models import CreateAccountRequest
from dishes.models import *

def signup(request):
    if request.method == "POST":
        form = CreateAccountRequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            CreateAccountRequest.objects.create(**form.cleaned_data)
            return redirect("index")
    else:
        form = CreateAccountRequestForm()

    context = {"form": form}
    return render(request, "registration/signup.html", context)
