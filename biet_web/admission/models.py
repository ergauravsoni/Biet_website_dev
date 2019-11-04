from django.db import models

# Create your models here.
class UG_addmission(models.Model):
    addmission_fee = models.FileField(upload_to = 'addmission/UG/')
    CourseWiseSeatMatrix = models.FileField(upload_to = 'addmission/UG/')
    notification = models.FileField(upload_to = 'addmission/UG/')
    application_form = models.FileField(upload_to = 'addmission/UG/')
    cut_off = models.FileField(upload_to = 'addmission/UG/')

    def __str__(self):
        return '{}{}{}{}{}'.format(self.addmission_fee,self.CourseWiseSeatMatrix,self.notification,self.application_form,self.cut_off)

class PG_addmission(models.Model):
    CourseWiseSeatMatrix = models.FileField(upload_to = 'addmission/PG/')
    notification = models.FileField(upload_to = 'addmission/PG/', default='coming-soon.png')
    application_form = models.FileField(upload_to = 'addmission/PG/')
    cut_off = models.FileField(upload_to = 'addmission/PG/', default='coming-soon.png')

    def __str__(self):
        return '{}{}{}{}'.format(self.CourseWiseSeatMatrix,self.notification,self.application_form,self.cut_off)
