from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("After GIT, Rango says hey there partner!")
