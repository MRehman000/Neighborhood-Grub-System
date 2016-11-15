from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, word. You're at the dishes index.")
