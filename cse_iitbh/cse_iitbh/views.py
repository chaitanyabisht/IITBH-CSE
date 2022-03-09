from django.http import HttpResponse
from django.shortcuts import render

<<<<<<< HEAD
import requests as r
import requests as r

def course_list():
    lst = r.get('https://api.github.com/orgs/IIT-Bhilai-CSE/repos?type=all').json()
    return [item['name'] for item in lst]
=======
>>>>>>> f35c2296129a6aa073b15555110d8cc9275c2d9d

def homepage(request):
    return render(request,'homepage.html')

def ycse(request):
    return render(request,'y_index.html')
<<<<<<< HEAD

def courses(request):
    context = {"course_list":course_list()}
    return render(request, 'courses.html', context)
=======
>>>>>>> f35c2296129a6aa073b15555110d8cc9275c2d9d
