from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    category=models.CharField(max_length=90)
    user_image = models.ImageField(upload_to="static/images/",default='path/to/placeholder.jpg')
    def __str__(self):
        return self.username