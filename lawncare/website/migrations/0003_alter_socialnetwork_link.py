# Generated by Django 3.2.3 on 2021-05-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_newsletter_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialnetwork',
            name='link',
            field=models.URLField(verbose_name='url'),
        ),
    ]