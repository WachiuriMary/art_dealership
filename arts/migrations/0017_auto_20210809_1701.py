# Generated by Django 3.1.7 on 2021-08-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0016_auto_20210808_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='artphoto',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to=''),
        ),
    ]
