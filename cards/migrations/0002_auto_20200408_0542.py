# Generated by Django 3.0.4 on 2020-04-08 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='dob',
            new_name='DOB',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='team',
            new_name='name',
        ),
    ]
