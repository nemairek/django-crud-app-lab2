from django.db import models

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
