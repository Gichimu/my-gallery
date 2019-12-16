from django.test import TestCase
from .models import Image, Location, Category

class ImageTestClass(TestCase):

    def setUp(self):
        self.test_location = Location(name='Beach')
        self.test_location.save()
        self.test_category = Category(name='test-category')
        self.test_category.save()
        self.test_image = Image(image='test.jpg', name='test', description='An amazing image', location=self.test_location, category=self.test_category)


    def test_save_image(self):
        self.test_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        Image.delete_image(self.test_image.id)
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.test_image.update_image(self.test_image.id, name='another')
        self.assertTrue(self.test_image.name == 'another')

    def test_get_image_by_id(self):
        image = Image.get_image_by_id(self.test_image.id)
        self.assertEqual(image.name, self.test_image.name)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        