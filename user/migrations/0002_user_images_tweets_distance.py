# Generated by Django 4.2 on 2023-08-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='images_tweets_distance',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
