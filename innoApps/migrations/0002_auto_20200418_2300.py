# Generated by Django 3.0.5 on 2020-04-18 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innoApps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instruction', models.CharField(max_length=300)),
                ('mix', models.IntegerField()),
                ('match', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='instruction',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='match',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='mix',
        ),
    ]