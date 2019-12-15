from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, 'home.html')

def search(request):
    
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        images = Image.search_image(category)
        message = f"{category}"

        return render(request, 'search_results.html',{"message":message,"images": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html',{"message":message})
