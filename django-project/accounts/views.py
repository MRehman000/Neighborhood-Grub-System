from django.shortcuts import render, redirect

from accounts.forms import *
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
            print(form.cleaned_data)
            choice = int(form.cleaned_data["choice"])
            if choice == TerminateAccountRequestForm.YES:
                TerminateAccountRequest.objects.create(user=request.user)
                context["request_confirmed"] = True
            else:
                return redirect("account")
    else:
        form = TerminateAccountRequestForm()
    context["form"] = form
    print(context)
    return render(request, "accounts/user_confirm_terminate.html", context)
