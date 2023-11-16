from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def india(request):
    return HttpResponse('<h1>india qualified for finals</h1>')
def login(request):
    d={'username':'dileep'}
    return render(request,'login.html',context=d)
