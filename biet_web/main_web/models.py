from django.db import models
import datetime

# Create your models here.
class Event(models.Model):
    event_date = models.DateField()
    venue = models.CharField(max_length=200)
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.event_name)

class News(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=200)
    detail = models.FileField(upload_to = 'main_web/latest/')

    def __str__(self):
        return '{}'.format(self.title)

class Gallary(models.Model):
    images = models.ImageField(upload_to='main_gallary')
    
    def __str__(self):
        return '{}'.format(self.images)


