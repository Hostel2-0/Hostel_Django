# Generated by Django 4.1.7 on 2023-03-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhostel', '0002_alter_hostel_options_alter_towns_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
