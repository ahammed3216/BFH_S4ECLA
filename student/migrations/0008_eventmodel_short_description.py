# Generated by Django 2.2.20 on 2021-05-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_eventmodel_approve_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='short_description',
            field=models.CharField(default='nice programme', max_length=50),
            preserve_default=False,
        ),
    ]
