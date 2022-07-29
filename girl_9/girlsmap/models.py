from django.db import models

# Create your models here.

class bar(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=100, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)
    information=models.TextField(max_length=200)
    photo=models.ImageField(blank=True, null=True, upload_to="bar_photo")

    def __str__(self):
        return self.name


