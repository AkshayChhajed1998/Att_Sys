# Generated by Django 2.0.8 on 2018-09-06 16:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0003_auto_20180906_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('student_id', models.CharField(blank=True, default='', max_length=7, null=True)),
                ('image_s', models.ImageField(blank=True, default='', upload_to='profilepics/')),
                ('mobile_number_s', models.BigIntegerField(blank=True, default=9999999999)),
                ('parents_number_s', models.BigIntegerField(blank=True, default=9999999999)),
                ('department', models.CharField(blank=True, default='', max_length=40)),
                ('Semester', models.PositiveSmallIntegerField(blank=True)),
                ('dob', models.DateField(blank=True, default=datetime.datetime.now)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('roll_no', models.CharField(max_length=6)),
                ('section', models.CharField(default='', max_length=1)),
            ],
        ),
    ]
