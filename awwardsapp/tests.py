from django.test import TestCase
from . models import Projects, Profile, Rating

# Create your tests here.

# Profile model test  
      
class ProfileTestClass(TestCase):        
    
        # Set up method
    def setUp(self):
        self.image= Profile(profile_pict = 'img.jpg', bio ='image')
        # self.images= Profile(profile1 = 'piza1.jpg', bio ='pizza')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))     
