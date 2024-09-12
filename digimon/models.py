from django.db import models
from django.urls import reverse

# Create your models here.
class Digimon(models.Model):
    digid = models.IntegerField()
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    attribute = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse("digimon_detail", kwargs={"digimon_id": self.id})

class Move(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('move_detail', kwargs={'pk': self.id})
    

