# Generated by Django 4.1.6 on 2023-02-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_alter_report_created_alter_report_location_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
