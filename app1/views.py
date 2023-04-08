from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_first(request):
    return HttpResponse('<h1>This ia app1 first page</h1>')

def app1_second(request):
    return HttpResponse('<h1>This ia app1 second page</h1>')
