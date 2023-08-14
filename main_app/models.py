from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    category = models.CharField(max_length=100)
    latest_model = models.BooleanField()

    def __str__(self):
        return self.name


