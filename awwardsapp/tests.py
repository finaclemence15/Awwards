from django.test import TestCase
from . models import Projects, Profile, Rating

# Create your tests here.

# Profile model test  
      
class ProfileTestClass(TestCase):        
    
        # Set up method
    def setUp(self):
        self.image= Profile(profile_pict = 'img.jpg', bio ='image', email = "fi@gmail.com",phone_number = '07854222')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))     

        # Testing Save Method of Profile model
    def test_save_method(self):
        self.image.save_profile()
        images = Profile.objects.all()
        self.assertTrue(len(images) > 0)   
        
    # Testing  delete method of Profile model     
    def test_delete(self):
        self.image= Profile(profile_pict = 'img.jpg', bio ='image')
        self.image.save_profile()
        image = Profile.objects.filter(profile_pict = 'img.jpg').first()
        delete = Profile.objects.filter(id = image.id).delete()
        images = Profile.objects.all()
        self.assertTrue(len(images) == 0)         

    # Testing  update method of Profile model    
    def test_update(self):
        self.image.save_profile()
        image = Profile.objects.filter(profile_pict = 'img.jpg').first()
        update = Profile.objects.filter(id = image.id).update(profile_pict = 'cake.jpg')
        updated = Profile.objects.filter(profile_pict = 'cake.jpg').first()
        self.assertNotEqual(image.profile_pict, updated.profile_pict)         
        
# Projects model test  
      
class ProjectsTestClass(TestCase):        
    
        # Set up method
    def setUp(self):
        self.pizza= Projects(title = 'pizza',image = 'img.jpg', description ='delicious',post_date = '07854222')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pizza,Projects))
        
        # Testing Save Method of Project model
    def test_save_method(self):
        self.pizza.save_projects()
        pizza1 = Projects.objects.all()
        self.assertTrue(len(pizza1) > 0)                    