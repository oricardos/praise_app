# Generated by Django 4.1.5 on 2023-01-10 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_alter_song_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_posted',
            field=models.BooleanField(default=True),
        ),
    ]
