from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField('Name', max_length=12)
    father = models.CharField('father', max_length=12, blank=True)
    age = models.IntegerField('Age', blank=True)

    def __str__(self):
        return self.name

