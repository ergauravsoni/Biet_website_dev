from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Academic_Calender(models.Model):
    calender = models.FileField(upload_to = 'about_biet/calender/')

    def __str__(self):
        return '{}'.format(self.calender)

class Office_Staff(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_biet/office/image/')
    detail = models.FileField(upload_to='about_biet/office/data/')
    sno = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)

class Deans(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    responsibility = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    contact_no = PhoneNumberField()
    image = models.ImageField(upload_to='about_biet/deans/image/')
    description = models.TextField()
    detail = models.FileField(upload_to='about_biet/deans/data/')
    
    def __str__(self):
        return self.name + ": " + self.responsibility
        
class Governing_Body(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(default='',upload_to='about_biet/governing_body/image/')

    def __str__(self):
        return self.name + ": " + self.designation

class Governing_Council(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(default='',upload_to='about_biet/governing_council/image/')

    def __str__(self):
        return self.name + ": " + self.designation
