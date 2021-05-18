# Generated by Django 2.2.20 on 2021-05-17 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0003_orderevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='start_date',
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('ref_code', models.CharField(max_length=30)),
                ('events', models.ManyToManyField(to='student.OrderEvent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
