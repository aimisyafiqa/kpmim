# Generated by Django 5.1 on 2024-08-21 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('mentorcode', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('mentor_name', models.TextField()),
            ],
        ),
    ]
