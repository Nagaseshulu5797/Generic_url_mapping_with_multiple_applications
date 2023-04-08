from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_first(request):
    return HttpResponse('<h1>This ia app2 first page</h1>')

def app2_second(request):
    return HttpResponse('<h1>This ia app2 second page</h1>')