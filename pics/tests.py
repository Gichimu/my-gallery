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
        self.test_image.save_image()
        new_name = 'nature'
        self.test_image.update_image(id=self.test_image.id, name=new_name)
        new_image = Image.objects.get(id=self.test_image.id)
        self.assertEqual(new_image.name, 'nature')

    def test_get_image_by_id(self):
        self.my_test_image = Image(image='images/new_image.jpg', name='new_image', description='a nice image', location=self.test_location, category=self.test_category)
        self.my_test_image.save_image()
        image = Image.get_image_by_id(self.my_test_image.id)
        self.assertEqual(image.name, self.my_test_image.name)

    def test_filter_by_location(self):
        self.my_test_image = Image(image='images/new_image.jpg', name='new_image', description='a nice image', location=self.test_location, category=self.test_category)
        self.my_test_image.save_image()
        self.test_image.save_image()
        images = Image.filter_by_location(self.test_location)
        self.assertTrue(len(images) == 2)

    def test_search_images(self):
        self.my_test_image = Image(image='images/new_image.jpg', name='new_image', description='a nice image', location=self.test_location, category=self.test_category)
        self.my_test_image.save_image()
        self.test_image.save_image()
        images = Image.search_images(self.test_category)
        self.assertTrue(len(images) == 2)

        # Category model tests #
    def test_save_category(self):
        self.test_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.test_category.save_category()
        self.test_category.delete_category(self.test_category.id)
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

    def test_update_category(self):
        self.test_category.save_category()
        self.test_category.update_category(id=self.test_category.id, name='new_category')
        category = Category.objects.get(id=self.test_category.id)
        self.assertEqual(category.name, 'new_category')


        # Location model tests #

    def test_save_location(self):
        self.test_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.test_location.save_location()
        self.test_location.delete_location(self.test_location.id)
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_update_location(self):
        self.test_location.save_location()
        self.test_location.update_location(id=self.test_location.id, name='new_location')
        location = Location.objects.get(id=self.test_location.id)
        self.assertEqual(location.name, 'new_location')

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        