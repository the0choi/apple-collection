from django.db import models
from django.urls import reverse


class Accessory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})


class Device(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    type = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'device_id': self.id})


class Version(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.IntegerField()

    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} on {self.release_year}"

    class Meta:
        ordering = ['-release_year']
