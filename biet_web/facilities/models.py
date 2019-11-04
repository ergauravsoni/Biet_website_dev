from django.db import models

# Create your models here.
class Sport(models.Model):
    reports = models.FileField(upload_to = 'facilities/Sport/')

    def __str__(self):
        return '{}'.format(self.reports)


