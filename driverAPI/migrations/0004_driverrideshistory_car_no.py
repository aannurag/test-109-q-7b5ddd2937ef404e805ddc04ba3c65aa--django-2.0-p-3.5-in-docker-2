# Generated by Django 2.1.2 on 2018-10-23 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driverAPI', '0003_remove_driverrideshistory_distance_travelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverrideshistory',
            name='car_no',
            field=models.CharField(default=django.utils.timezone.now, max_length=80, unique=True),
            preserve_default=False,
        ),
    ]
