# Generated by Django 3.0.6 on 2020-06-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0019_computer_science_dept_book_chapters_computer_science_dept_publications'),
    ]

    operations = [
        migrations.CreateModel(
            name='computer_science_dept_accreditation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('designation', models.TextField()),
                ('member_type', models.CharField(choices=[('PAC', 'Program Assessment Committee (PAC)'), ('DAB', 'Department Advisory Board (DAB)')], default='DAB', max_length=10)),
            ],
        ),
    ]