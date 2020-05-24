from django.db import models

# Create your models here.


class civil_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/CV/image/')
    detail = models.FileField(upload_to='department/CV/data/')

    def __str__(self):
        return '{}'.format(self.name)


class civil_depatment_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class mechanical_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/ME/image/')
    detail = models.FileField(upload_to='department/ME/data/')

    def __str__(self):
        return '{}'.format(self.name)


class mechanical_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class biotechnology_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/BT/image/')
    detail = models.FileField(upload_to='department/BT/data/')

    def __str__(self):
        return '{}'.format(self.name)


class biotechnology_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class chemical_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/CH/image/')
    detail = models.FileField(upload_to='department/CH/data/')

    def __str__(self):
        return '{}'.format(self.name)


class chemical_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class chemistry_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/CHE/image/')
    detail = models.FileField(upload_to='department/CHE/data/')

    def __str__(self):
        return '{}'.format(self.name)


class chemistry_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class computer_science_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/CS/image/')
    detail = models.FileField(upload_to='department/CS/data/')

    def __str__(self):
        return '{}'.format(self.name)


class computer_science_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/PhotoGallery/')

    def __str__(self):
        return '{}'.format(self.image)


class electronics_and_communication_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/EC/image/')
    detail = models.FileField(upload_to='department/EC/data/')

    def __str__(self):
        return '{}'.format(self.name)


class electronics_and_communication_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class electrical_and_electronics_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/EEE/image/')
    detail = models.FileField(upload_to='department/EEE/data/')

    def __str__(self):
        return '{}'.format(self.name)


class electrical_and_electronics_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class information_science_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/IS/image/')
    detail = models.FileField(upload_to='department/IS/data/')

    def __str__(self):
        return '{}'.format(self.name)


class information_science_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class mathematics_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/MAT/image/')
    detail = models.FileField(upload_to='department/MAT/data/')

    def __str__(self):
        return '{}'.format(self.name)


class mathematics_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class physics_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/PHY/image/')
    detail = models.FileField(upload_to='department/PHY/data/')

    def __str__(self):
        return '{}'.format(self.name)


class physics_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class textile_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/TX/image/')
    detail = models.FileField(upload_to='department/TX/data/')

    def __str__(self):
        return '{}'.format(self.name)


class textile_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class mca_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/MCA/image/')
    detail = models.FileField(upload_to='department/MCA/data/')

    def __str__(self):
        return '{}'.format(self.name)


class mca_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class environmental_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/ENV/image/')
    detail = models.FileField(upload_to='department/ENV/data/')

    def __str__(self):
        return '{}'.format(self.name)


class environmental_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)


class computer_science_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name


class computer_science_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."


class computer_science_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name


class computer_science_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
        return self.achievement_description[:50] + "..."


class computer_science_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/CS/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section


class computer_science_dept_events(models.Model):
    events = models.FileField(upload_to='department/CS/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)


class computer_science_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/CS/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)


class computer_science_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name


class computer_science_dept_research_scholars(models.Model):

    year_choices_array = []
    for year in range(1979, 2021):
        year_choices_array.append((year, year))
    year_choices_array.append((0, 'NA'))
    year_choices = tuple(year_choices_array)
    research_scholar_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year_of_regn = models.IntegerField(choices=year_choices, default=0)
    phD = models.CharField(max_length=10, choices=(
        ('PHD', 'Ph.D.'), ('(PHD)', '(Ph.D.)')), default='(PHD)')
    course_work_completed = models.CharField(
        max_length=1, choices=(('Y', 'Yes'), ('N', 'No')), default='Y')
    pre_phD_viva_voce = models.CharField(
        max_length=1, choices=(('Y', 'Yes'), ('N', 'No')), default='Y')
    submitted_final_thesis = models.CharField(
        max_length=1, choices=(('Y', 'Yes'), ('N', 'No')), default='Y')
    phD_awarded_year = models.IntegerField(choices=year_choices, default=0)
    guide = models.ForeignKey(
        computer_science_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name
