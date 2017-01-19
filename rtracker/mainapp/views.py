from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Placeholder on main index page.")
# Create your views here.
