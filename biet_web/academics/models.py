from django.db import models

# Create your models here.
class Library_User_Manual(models.Model):
    user_manual = models.FileField(upload_to = 'academics/library/user_manual/')

    def __str__(self):
        return '{}'.format(self.user_manual)

class Gallary(models.Model):
    image = models.ImageField(upload_to = 'academics/library/gallary/')

    def __str__(self):
        return '{}'.format(self.image)
