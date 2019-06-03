from django.db import models

# Create your models here.

class MainImgs(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='main_imgs')

    def __str__(self):
        return f'{self.title} Image'
