# Generated by Django 3.2.3 on 2021-05-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_delete_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tips',
            name='image',
            field=models.FileField(upload_to='img'),
        ),
    ]
