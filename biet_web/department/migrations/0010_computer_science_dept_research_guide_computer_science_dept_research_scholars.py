# Generated by Django 3.0.6 on 2020-05-23 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0009_auto_20200523_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='computer_science_dept_research_guide',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False)),
                ('guide_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='computer_science_dept_research_scholars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_scholar_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('year_of_regn', models.IntegerField(choices=[(1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2020)),
                ('phD', models.CharField(choices=[('PHD', 'Ph.D.'), ('(PHD)', '(Ph.D.)')], default='(PHD)', max_length=10)),
                ('course_work_completed', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('pre_phD_viva_voce', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('submitted_final_thesis', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('phD_awarded_year', models.IntegerField(choices=[(1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2020)),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.computer_science_dept_research_guide')),
            ],
        ),
    ]
