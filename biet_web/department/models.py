from django.db import models

# Create your models here.


class civil_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/CV/image/')
    detail = models.FileField(upload_to='department/CV/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class civil_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class civil_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(civil_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class civil_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class civil_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class civil_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class civil_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class civil_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name
 
class civil_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."
        
class civil_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/CV/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class civil_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class civil_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/CV/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class civil_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type 

class civil_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name
 
class civil_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/CV/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class civil_dept_events(models.Model):
    events = models.FileField(upload_to='department/CV/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class civil_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CV/')

    def __str__(self):
        return '{}'.format(self.image)
        
class mechanical_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/ME/image/')
    detail = models.FileField(upload_to='department/ME/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type
        
class mechanical_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class mechanical_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(mechanical_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class mechanical_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class mechanical_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class mechanical_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class mechanical_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/ME/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class mechanical_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name


class mechanical_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class mechanical_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class mechanical_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/ME/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class mechanical_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type
        
class mechanical_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class mechanical_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/ME/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class mechanical_dept_events(models.Model):
    events = models.FileField(upload_to='department/ME/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class mechanical_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/ME/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class mechanical_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/ME/')

    def __str__(self):
        return '{}'.format(self.image)

class electrical_and_electronics_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/EE/image/')
    detail = models.FileField(upload_to='department/EE/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class electrical_and_electronics_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class electrical_and_electronics_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(electrical_and_electronics_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class electrical_and_electronics_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class electrical_and_electronics_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class electrical_and_electronics_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class electrical_and_electronics_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/EE/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class electrical_and_electronics_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class electrical_and_electronics_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class electrical_and_electronics_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/EE/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class electrical_and_electronics_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class electrical_and_electronics_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/EE/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class electrical_and_electronics_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class electrical_and_electronics_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class electrical_and_electronics_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/EE/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class electrical_and_electronics_dept_events(models.Model):
    events = models.FileField(upload_to='department/EE/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class electrical_and_electronics_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/EE/')

    def __str__(self):
        return '{}'.format(self.image)

class electronics_and_communication_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/EC/image/')
    detail = models.FileField(upload_to='department/EC/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class electronics_and_communication_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class electronics_and_communication_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(electronics_and_communication_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class electronics_and_communication_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class electronics_and_communication_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class electronics_and_communication_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class electronics_and_communication_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/EC/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class electronics_and_communication_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class electronics_and_communication_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class electronics_and_communication_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/EC/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class electronics_and_communication_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class electronics_and_communication_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/EC/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class electronics_and_communication_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class electronics_and_communication_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class electronics_and_communication_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/EC/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class electronics_and_communication_dept_events(models.Model):
    events = models.FileField(upload_to='department/EC/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class electronics_and_communication_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/EC/')

    def __str__(self):
        return '{}'.format(self.image)

class chemical_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/CH/image/')
    detail = models.FileField(upload_to='department/CH/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class chemical_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class chemical_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(chemical_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class chemical_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class chemical_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class chemical_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class chemical_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/CH/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class chemical_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class chemical_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class chemical_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/CH/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class chemical_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class chemical_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/CH/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class chemical_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class chemical_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class chemical_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/CH/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class chemical_dept_events(models.Model):
    events = models.FileField(upload_to='department/CH/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class chemical_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CH/')

    def __str__(self):
        return '{}'.format(self.image)

class electronics_and_instrumentation_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/EI/image/')
    detail = models.FileField(upload_to='department/EI/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class electronics_and_instrumentation_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class electronics_and_instrumentation_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(electronics_and_instrumentation_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class electronics_and_instrumentation_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class electronics_and_instrumentation_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class electronics_and_instrumentation_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class electronics_and_instrumentation_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/EI/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class electronics_and_instrumentation_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class electronics_and_instrumentation_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class electronics_and_instrumentation_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/EI/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class electronics_and_instrumentation_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class electronics_and_instrumentation_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/EI/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class electronics_and_instrumentation_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class electronics_and_instrumentation_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class electronics_and_instrumentation_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/EI/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class electronics_and_instrumentation_dept_events(models.Model):
    events = models.FileField(upload_to='department/EI/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class electronics_and_instrumentation_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/EI/')

    def __str__(self):
        return '{}'.format(self.image)

class computer_science_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/CS/image/')
    detail = models.FileField(upload_to='department/CS/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

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
    guide = models.ForeignKey(computer_science_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class computer_science_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class computer_science_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class computer_science_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class computer_science_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/CS/laboratory/')

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

class computer_science_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/CS/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class computer_science_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class computer_science_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/CS/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class computer_science_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
        return self.achievement_description[:50] + "... : " + self.achievement_type 

class computer_science_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

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

class computer_science_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/PhotoGallery/')

    def __str__(self):
        return '{}'.format(self.image)

class information_science_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/IS/image/')
    detail = models.FileField(upload_to='department/IS/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class information_science_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class information_science_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(information_science_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class information_science_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class information_science_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class information_science_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class information_science_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/IS/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class information_science_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class information_science_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class information_science_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/IS/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class information_science_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class information_science_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/IS/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class information_science_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class information_science_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class information_science_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/IS/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class information_science_dept_events(models.Model):
    events = models.FileField(upload_to='department/IS/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class information_science_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/IS/')

    def __str__(self):
        return '{}'.format(self.image)

class textile_technology_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/TX/image/')
    detail = models.FileField(upload_to='department/TX/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class textile_technology_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class textile_technology_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(textile_technology_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class textile_technology_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class textile_technology_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class textile_technology_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class textile_technology_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/TX/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class textile_technology_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class textile_technology_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class textile_technology_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/TX/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class textile_technology_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class textile_technology_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/TX/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class textile_technology_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class textile_technology_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class textile_technology_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/TX/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class textile_technology_dept_events(models.Model):
    events = models.FileField(upload_to='department/TX/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class textile_technology_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/TX/')

    def __str__(self):
        return '{}'.format(self.image)

class bio_technology_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/BT/image/')
    detail = models.FileField(upload_to='department/BT/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class bio_technology_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class bio_technology_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(bio_technology_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class bio_technology_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class bio_technology_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class bio_technology_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class bio_technology_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/BT/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class bio_technology_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class bio_technology_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class bio_technology_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/BT/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class bio_technology_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class bio_technology_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/BT/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class bio_technology_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class bio_technology_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class bio_technology_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/BT/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class bio_technology_dept_events(models.Model):
    events = models.FileField(upload_to='department/BT/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class bio_technology_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/BT/')

    def __str__(self):
        return '{}'.format(self.image)

class physics_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/PHY/image/')
    detail = models.FileField(upload_to='department/PHY/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class physics_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class physics_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(physics_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class physics_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class physics_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class physics_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class physics_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/PHY/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class physics_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class physics_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class physics_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/PHY/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class physics_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class physics_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class physics_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class physics_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/PHY/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class physics_dept_events(models.Model):
    events = models.FileField(upload_to='department/PHY/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class physics_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/PHY/')

    def __str__(self):
        return '{}'.format(self.image)

class chemistry_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/CHEM/image/')
    detail = models.FileField(upload_to='department/CHEM/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class chemistry_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class chemistry_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(chemistry_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class chemistry_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class chemistry_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class chemistry_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class chemistry_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/CHEM/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class chemistry_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class chemistry_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class chemistry_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/CHEM/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class chemistry_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class chemistry_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class chemistry_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class chemistry_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/CHEM/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class chemistry_dept_events(models.Model):
    events = models.FileField(upload_to='department/CHEM/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class chemistry_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/CHEM/')

    def __str__(self):
        return '{}'.format(self.image)

class mathematics_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/MAT/image/')
    detail = models.FileField(upload_to='department/MAT/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class mathematics_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class mathematics_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(mathematics_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class mathematics_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class mathematics_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class mathematics_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class mathematics_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/MAT/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class mathematics_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class mathematics_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class mathematics_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/MAT/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class mathematics_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class mathematics_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class mathematics_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class mathematics_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/MAT/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class mathematics_dept_events(models.Model):
    events = models.FileField(upload_to='department/MAT/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class mathematics_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/MAT/')

    def __str__(self):
        return '{}'.format(self.image)

class bio_medical_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/BM/image/')
    detail = models.FileField(upload_to='department/BM/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('HOD', 'Head Of Department'),
        ('FACULTY', 'Faculty Member'),
        ('TECHNICAL', 'Technical Staff'),
        ('SUPPORTING', 'Supporting Staff')), default='FACULTY')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class bio_medical_dept_research_guide(models.Model):
    sno = models.IntegerField(primary_key=True)
    guide_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guide_name

class bio_medical_dept_research_scholars(models.Model):

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
    guide = models.ForeignKey(bio_medical_dept_research_guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.research_scholar_name

class bio_medical_dept_publications(models.Model):
    name_of_faculty = models.CharField(max_length=100)
    y15 = models.IntegerField(blank=True,null=True)
    y16 = models.IntegerField(blank=True,null=True)
    y17 = models.IntegerField(blank=True,null=True)
    y18 = models.IntegerField(blank=True,null=True)
    y19 = models.IntegerField(blank=True,null=True)
    national_or_inter = models.CharField(max_length=13)
    indexing = models.CharField(max_length=500, blank=True,null=True)
    citations = models.IntegerField(blank=True,null=True)
    impact_factor = models.CharField(max_length=80, blank=True,null=True)
    i10_index = models.IntegerField(blank=True,null=True)
    h_index = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name_of_faculty

class bio_medical_dept_book_chapters(models.Model):
    sl_no = models.IntegerField()
    name_of_book_chapter = models.CharField(max_length=500)
    names_of_authors = models.CharField(max_length=500)
    year_of_pub = models.IntegerField()
    name_of_pub = models.CharField(max_length=500)

    def __str__(self):
        return self.name_of_book_chapter

class bio_medical_dept_grants_and_patents(models.Model):
    description = models.TextField()
    grant_or_patent = models.CharField(max_length=500, choices=(
        ('GRANT', 'Grant'), ('PATENT', 'Patent')), default='GRANT')

    def __str__(self):
         return self.description[:50] + "... : " + self.grant_or_patent

class bio_medical_dept_laboratory_facilities_gallary(models.Model):
    image = models.ImageField(upload_to='department/gallery/BM/laboratory/')

    def __str__(self):
        return '{}'.format(self.image)

class bio_medical_dept_lab_facilities(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    config_specs = models.TextField()
    softwares = models.TextField()

    def __str__(self):
        return self.name

class bio_medical_dept_major_equipments(models.Model):
    equipment_description = models.TextField()

    def __str__(self):
        return self.equipment_description[:50] + "..."

class bio_medical_dept_classroom(models.Model):
    classroom = models.FileField(upload_to='department/BM/data/classroom/')

    def __str__(self):
        return '{}'.format(self.classroom)

class bio_medical_dept_accreditation(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.TextField(blank=True)
    member_type = models.CharField(max_length=100, choices=(
        ('PAC', 'Program Assessment Committee (PAC)'),
        ('DAB', 'Department Advisory Board (DAB)')), default='DAB')

    def __str__(self):
        return self.name + " : " + self.member_type

class bio_medical_dept_alumni(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='department/alumni/BM/')
    sno = models.IntegerField(default='1')
    
    def __str__(self):
        return self.name + ":" + self.designation

class bio_medical_dept_achievements(models.Model):
    achievement_description = models.TextField()
    achievement_type = models.CharField(max_length=500, choices=(
        ('STUDENT', 'Student Achievement'), ('STAFF', 'Staff Achievement')), default='STAFF')

    def __str__(self):
         return self.achievement_description[:50] + "... : " + self.achievement_type

class bio_medical_dept_activities(models.Model):
    sno = models.IntegerField()
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    activity_type = models.CharField(max_length=500, choices=(
        ('RE', 'Regular Event'), ('STC', 'Short-term Course')), default='RE')

    def __str__(self):
        return self.activity_name

class bio_medical_dept_timetable(models.Model):
    course = models.CharField(max_length=100, choices=(
        ('BE', 'B.E.'), ('MT', 'M.Tech')), default='BE')
    semester = models.IntegerField()
    section = models.CharField(max_length=1)
    timetable = models.FileField(upload_to='department/BM/data/timetable/')

    def __str__(self):
        return self.course + ": " + str(self.semester) + "-" + self.section

class bio_medical_dept_events(models.Model):
    events = models.FileField(upload_to='department/BM/data/events/')
    semester = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.events)

class bio_medical_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/BM/')

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
    image = models.ImageField(upload_to='department/gallery/MCA/')

    def __str__(self):
        return '{}'.format(self.image)


class environmental_dept(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='department/ENV/image/')
    detail = models.FileField(upload_to='department/ENV/data/')
    sno = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)


class environmental_dept_gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery/ENV/')

    def __str__(self):
        return '{}'.format(self.image)
