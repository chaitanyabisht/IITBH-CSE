from django.http import HttpResponse
from django.shortcuts import render

import requests as r
import requests as r

def course_list():
    lst = r.get('https://api.github.com/orgs/IIT-Bhilai-CSE/repos?type=all').json()
    return [item['name'] for item in lst]

def homepage(request):
    return render(request,'homepage.html')

def ycse(request):
    return render(request,'y_index.html')

def courses(request):
    context = {"course_list":course_list()}
    return render(request, 'courses.html', context)
