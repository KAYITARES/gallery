from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.Rwanda= Location(photo_location="Rwanda")
        self.Rwanda.save_location()
       #Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Rwanda,Location)) 
    # Testing Save Method
    def test_save_method(self):
        self.Rwanda.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
    def test_updating_location(self):
        location = Location.get_location_id(self.Rwanda.id)
        location.update_location('Kitengela')
        location = Location.get_location_id(self.Rwanda.id)
        self.assertTrue(location.photo_location == 'Kitengela')
    def tearDown(self):
        self.Rwanda.delete_location()
