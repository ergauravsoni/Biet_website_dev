# Generated by Django 3.0.6 on 2020-07-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_biet', '0006_governing_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='governing_body',
            name='image',
            field=models.ImageField(default='', upload_to='about_biet/governing_body/image/'),
        ),
    ]
