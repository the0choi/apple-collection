from django.db import models
from django.urls import reverse

class Device(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    category = models.CharField(max_length=100)
    colours = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'device_id': self.id})

