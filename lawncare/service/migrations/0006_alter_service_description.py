# Generated by Django 3.2.3 on 2021-05-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
