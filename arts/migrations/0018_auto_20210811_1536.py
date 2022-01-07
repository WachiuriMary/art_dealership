# Generated by Django 3.1.7 on 2021-08-11 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0017_auto_20210809_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistprofile',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='artistprofile',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='artistprofile',
            old_name='artprof',
            new_name='profile_pic',
        ),
        migrations.RenameField(
            model_name='customerprofile',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customerprofile',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='customerprofile',
            old_name='custprof',
            new_name='profile_pic',
        ),
    ]
