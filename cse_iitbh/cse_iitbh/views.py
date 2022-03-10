from django.http import HttpResponse
from django.shortcuts import render
import requests



def homepage(request):
    return render(request,'homepage.html')

def home(request):
    return render(request,'homepage.html')

def course_list():
    lst = requests.get('https://api.github.com/orgs/IIT-Bhilai-CSE/repos?type=all').json()
    return [item['name'] for item in lst]


def ycse(request):
    return render(request,'y_index.html')

def courses(request):
    context = {"course_list":course_list()}
    return render(request, 'courses.html', context)

def faculty(request):
    return render(request, "faculty.html")
