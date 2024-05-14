from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Hello, Django!</h1>")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<h1>Hello, Lucy!</h1>")

def contact(request):
    return HttpResponse("<h1>Hello, Pronit!</h1>")