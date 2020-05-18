from django.db import models

# Create your models here.
class Placement_Invitaton_For_Company(models.Model):
    invitation = models.FileField(upload_to = 'placement/')

    def __str__(self):
        return '{}'.format(self.invitation)

class Placement_Brochure(models.Model):
    brochure = models.FileField(upload_to = 'placement/')

    def __str__(self):
        return '{}'.format(self.brochure)


class Gallary(models.Model):
    image = models.FileField(upload_to = 'placement/gallary/')

    def __str__(self):
        return '{}'.format(self.image)
