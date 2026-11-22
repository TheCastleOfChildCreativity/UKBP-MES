from django.shortcuts import render
from django.http import HttpResponse 

def detail(request):
    return HttpResponse("detail")

def index(request):
    return HttpResponse("index")
