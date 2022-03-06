from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'homepage.html')

def ycse(request):
    return render(request,'y_index.html')
