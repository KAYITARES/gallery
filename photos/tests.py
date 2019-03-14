from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.Rwanda= Location(photo_location="Rwanda")
