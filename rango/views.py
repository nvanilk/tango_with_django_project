from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey  there partner! <br/> <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango is an application to enable users to rank various items and categories... <a href='/rango/' >Index<\a>")



