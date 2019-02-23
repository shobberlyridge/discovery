from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index - Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

def about(request):
	return HttpResponse("About - Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")

# def about(request):
# 	return HttpResponse("About - Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")
