# Generated by Django 2.2.20 on 2021-05-23 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_eventmodel_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
