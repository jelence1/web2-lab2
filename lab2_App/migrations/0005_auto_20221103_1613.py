# Generated by Django 3.2.16 on 2022-11-03 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab2_App', '0004_auto_20221102_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
        migrations.AddField(
            model_name='teams',
            name='lost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teams',
            name='played',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teams',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teams',
            name='won',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='user', max_length=1000),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goals1', models.IntegerField(null=True)),
                ('goals2', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='team1', to='lab2_App.teams')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='team2', to='lab2_App.teams')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab2_App.matches')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab2_App.users')),
            ],
        ),
    ]
