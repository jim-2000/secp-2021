from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to ="album/photos/")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    