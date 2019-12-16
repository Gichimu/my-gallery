from django.db import models
from django.utils import timezone

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to= 'images/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, default='')
    category = models.ForeignKey(Category, default='')

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(image_id):
        Image.objects.filter(id=image_id).delete()

    def update_image():
        Image.objects.filter(id=id).update(field = new_name) 

    @classmethod
    def search_images(cls, category):
        category = Category.objects.get(name=category)
        images = cls.objects.filter(category=category.id)
        return images

