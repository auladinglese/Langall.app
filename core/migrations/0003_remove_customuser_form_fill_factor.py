# Generated by Django 2.2.6 on 2019-11-17 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_teacherprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='form_fill_factor',
        ),
    ]
