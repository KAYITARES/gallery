from django.db import models

# Create your models here.
class Location(models.Model):
    photo_location = models.CharField(max_length=50)

    def __str__(self):
        return self.photo_location
class Category(models.Model):
    photo_category = models.CharField(max_length=50)

    def __str__(self):
        return self.photo_category
class Image(models.Model):
    image = models.ImageField(upload_to ='images/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
