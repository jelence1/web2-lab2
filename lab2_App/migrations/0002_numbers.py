# Generated by Django 3.2.16 on 2022-11-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab2_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
