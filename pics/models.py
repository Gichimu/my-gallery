from django.db import models

class Image(models.Model):
    image = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.image

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

