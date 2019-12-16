from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Category, Location

def welcome(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'home.html', {'images':images, 'categories':categories, 'locations':locations})

def search(request):
    
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        images = Image.search_images(category)
        message = f"{category}"

        return render(request, 'search_results.html',{"message":message,"images": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html',{"message":message})
