from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Image, Location, Category
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    title = 'Home'
    images = Image.get_all_images()
    return render(request, 'index.html', {'title':title, 'images':images})

def search(request):
    
    if 'category' in request.GET and request.GET['category']:
        search_category = request.GET.get('category')
        images_found = Image.search_image(search_category)
        message = f'{search_category}'

        return render(request, 'all-photos/search.html',{'message':message, 'images_found':images_found})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})