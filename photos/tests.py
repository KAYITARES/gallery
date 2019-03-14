from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.Rwanda= Location(photo_location="Rwanda")
       #Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Rwanda,Location)) 
