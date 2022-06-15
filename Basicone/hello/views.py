from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse ('<h1>Hi this is the successful deplyement of my website....Success<h1>')
