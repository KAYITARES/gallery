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
