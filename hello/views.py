from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def kimani(request):
    return render(request, "hello/kimani.html")

def pn(request):
    return render(request, "hello/pn.html")

def greet(request, name):
    return render(request, "hello/greet.html", {"name":name})
