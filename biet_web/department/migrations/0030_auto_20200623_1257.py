# Generated by Django 3.0.6 on 2020-06-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0029_bio_medical_dept_grants_and_patents_bio_technology_dept_grants_and_patents_chemical_dept_grants_and_'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio_medical_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='bio_technology_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='chemical_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='civil_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='computer_science_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='electrical_and_electronics_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='electronics_and_communication_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='electronics_and_instrumentation_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='information_science_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='mechanical_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='textile_technology_dept_alumni',
            name='sno',
            field=models.IntegerField(default='1'),
        ),
    ]