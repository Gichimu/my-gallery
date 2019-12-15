from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search_results.html')
