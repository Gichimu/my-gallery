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
    image = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, default='')
    category = models.ForeignKey(Category, default='')

    def __str__(self):
        return self.image

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_images(cls, category):
        category = Category.objects.filter(name=category)
        images = cls.objects.filter(category_id=category.id)
        return images

