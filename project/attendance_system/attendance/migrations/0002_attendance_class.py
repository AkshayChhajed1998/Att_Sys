# Generated by Django 2.0.8 on 2018-09-20 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.classes'),
        ),
    ]
