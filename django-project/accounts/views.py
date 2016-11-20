from django.shortcuts import render, redirect

from accounts.forms import ChefPermissionsRequestForm, CreateAccountRequestForm
from accounts.forms import TerminateAccountRequestForm

from accounts.models import *
from dishes.models import *

def signup(request):
    if request.method == "POST":
        form = CreateAccountRequestForm(request.POST)
        if form.is_valid():
            CreateAccountRequest.objects.create(**form.cleaned_data)
            return redirect("index")
    else:
        form = CreateAccountRequestForm()

    context = {"form": form}
    return render(request, "accounts/signup.html", context)

def account(request):
    context = {}
    return render(request, "accounts/account.html", context)

def terminate(request):
    context = {}
    if request.method == "POST":
        form = TerminateAccountRequestForm(request.POST)
        if form.is_valid():
            choice = int(form.cleaned_data["choice"])
            if choice == TerminateAccountRequestForm.YES:
                TerminateAccountRequest.objects.create(user=request.user)
                context["request_confirmed"] = True
            else:
                return redirect("account")
    else:
        form = TerminateAccountRequestForm()
    return render(request, "accounts/user_confirm_terminate.html", context)

def request_chef_permissions(request):
    context = {}
    if request.method == "POST":
        form = ChefPermissionsRequestForm(request.POST, request.FILES)
        if form.is_valid():
            ChefPermissionsRequest.objects.create(user=request.user,
                                                  **form.cleaned_data)
            context["request_confirmed"] = True
    else:
        form = ChefPermissionsRequestForm()

    context["form"] = form
    print(context)
    return render(request, "accounts/request-chef-permissions.html", context)
