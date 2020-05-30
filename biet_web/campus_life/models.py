from django.db import models

# Create your models here.
class Graduation_Day(models.Model):
    image = models.ImageField(upload_to = 'campus_life/graduation_day/image/')

    def __str__(self):
        return '{}'.format(self.image)

class NAAC(models.Model):
    brochure = models.FileField(upload_to = 'campus_life/NAAC/')

    def __str__(self):
        return '{}'.format(self.brochure)

class Btech_Technowav(models.Model):
    btech_technowav = models.FileField(upload_to = 'campus_life/btech_technowav/')
    type_id  = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.btech_technowav)
