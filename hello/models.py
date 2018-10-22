from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    desrtination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origin} to {self.desrtination} for {self.duration}"