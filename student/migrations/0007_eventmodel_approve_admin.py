# Generated by Django 2.2.20 on 2021-05-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20210519_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='approve_admin',
            field=models.BooleanField(default=True),
        ),
    ]
