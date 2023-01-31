# Generated by Django 4.1.5 on 2023-01-31 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_song_instrumental_file_song_voice_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='extra_voice',
            field=models.CharField(blank=True, help_text='Caso haja mais de um vídeo de vozes', max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='spotify',
            field=models.CharField(help_text='Link da música no Spotify', max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='voice_file',
            field=models.ImageField(blank=True, help_text='Arquivos úteis para vocal', upload_to='images/voices/%d/%m/%Y/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='voices',
            field=models.CharField(blank=True, help_text='Link com vídeo de separação de vozes', max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='ytmusic',
            field=models.CharField(help_text='Link da música no YouTube Music', max_length=200),
        ),
    ]
