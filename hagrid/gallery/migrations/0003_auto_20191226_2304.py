# Generated by Django 3.0 on 2019-12-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20190904_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
