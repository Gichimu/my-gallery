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

    def update_image(id, name):
        Image.objects.filter(id=id).update(name=name) 
    
    @classmethod
    def get_image_by_id(cls, id):
        try:
            image = cls.objects.get(id=id)
            print("Object found")
            return image
        except DoesNotExist:
            print("object not found")

    @classmethod
    def search_images(cls, category):
        category = Category.objects.get(name=category)
        images = cls.objects.filter(category=category.id)
        return images

