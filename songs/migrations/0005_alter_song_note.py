# Generated by Django 4.1.5 on 2023-01-10 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_remove_song_author_song_acoustic_guitar_song_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
