# Generated by Django 3.2.16 on 2022-11-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab2_App', '0002_numbers'),
    ]

    operations = [
        migrations.AddField(
            model_name='numbers',
            name='square',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]