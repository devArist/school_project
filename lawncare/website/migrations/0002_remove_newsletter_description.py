# Generated by Django 3.2.3 on 2021-05-20 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='description',
        ),
    ]
