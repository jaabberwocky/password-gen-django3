from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello there friend!</h1>")

def eggs(request):
    return HttpResponse("<h3>You got eggs?</h3>")