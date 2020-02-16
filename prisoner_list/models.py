from django.db import models


# Create your models here.
class Prisoner(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=32)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=32)

    def __str__(self):
        return self.name
