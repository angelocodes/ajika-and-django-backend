from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('</h1>Hello, welcome to the Job Board!</h1>')
