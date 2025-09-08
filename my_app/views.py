from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the my_app index.")    

def about(request):
    return HttpResponse("This is the about page.")

def add(request, a, b):
    return HttpResponse(f"The sum of {a} and {b} is {a + b}.")