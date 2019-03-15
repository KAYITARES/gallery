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
def single_image(request, category_name, image_id):
    # print(image_category)
    locations = Location.objects.all()

    image = Image.get_image_by_id(image_id)
    # Get category name
    # print(category_name)
    image_category = Image.objects.filter(category__photo_category = category_name)
    title = f'{category_name}'
    return render(request,'single_image.html',{'title':title, 'image':image, 'image_category':image_category, 'locations':locations})
