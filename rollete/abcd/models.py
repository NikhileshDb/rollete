from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class GameNumber(models.Model):
    number = models.PositiveIntegerField(validators=[MaxValueValidator(2)])
  
    def __str__(self):
        return str(self.id) + ' ' + str(self.number)


class Sign(models.Model):
    sign = models.CharField(max_length=1)

    def __str__(self):
        return str(self.id) + '  ' + self.sign


class Dozen(models.Model):
    dozen = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.id) + self.dozen

   
class Column(models.Model):
    column = models.CharField(max_length=10)
    def __str__(self):
        return str(self.id) + self.column
