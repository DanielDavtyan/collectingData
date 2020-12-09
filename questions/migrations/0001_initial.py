# Generated by Django 3.1.3 on 2020-12-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.BooleanField()),
                ('salary', models.TextField()),
                ('hobbies', models.TextField()),
                ('in_extrovert', models.BooleanField()),
                ('music_genre', models.TextField()),
                ('movie_genre', models.TextField()),
                ('gift', models.TextField()),
            ],
        ),
    ]
