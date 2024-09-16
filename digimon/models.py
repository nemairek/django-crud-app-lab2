from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Move(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('move_detail', kwargs={'pk': self.id})

class Digimon(models.Model):
    digid = models.IntegerField()
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    attribute = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    moves = models.ManyToManyField(Move)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse("digimon_detail", kwargs={"digimon_id": self.id})


    
class Digicrest(models.Model):
    name = models.CharField(max_length=100)


    digimon = models.ForeignKey(Digimon, on_delete=models.CASCADE)

    def __str__(self):
        return self.name