from django.db import models


# Create your models here.
class Academic_Calender(models.Model):
    calender = models.FileField(upload_to = 'about_biet/calender/')

    def __str__(self):
        return '{}'.format(self.calender)

class Office_Staff(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_biet/office/image/')
    detail = models.FileField(upload_to='department/office/data/')
    sno = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)

class EOA(models.Model):
    eoa = models.FileField(upload_to = 'about_biet/eoa/')

    def __str__(self):
        return '{}'.format(self.eoa)
