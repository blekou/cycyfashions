# Generated by Django 2.2.10 on 2020-07-13 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_trending2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trending2',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Trending',
        ),
        migrations.DeleteModel(
            name='Trending2',
        ),
    ]
