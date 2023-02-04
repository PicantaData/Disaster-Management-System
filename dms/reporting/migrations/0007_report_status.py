# Generated by Django 4.1.6 on 2023-02-04 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0006_rename_location_lat_report_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('R', 'Reported'), ('I', 'In Progress'), ('S', 'Solved')], default='R', max_length=1),
            preserve_default=False,
        ),
    ]
