# Generated by Django 2.2.10 on 2020-07-19 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
