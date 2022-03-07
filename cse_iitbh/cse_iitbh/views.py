from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")


def faculty(request):
    return render(request, "faculty.html")
