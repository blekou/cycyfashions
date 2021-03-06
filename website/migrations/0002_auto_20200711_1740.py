# Generated by Django 2.2.10 on 2020-07-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reseaux_sociaux',
            options={'verbose_name': 'reseaux sociaux', 'verbose_name_plural': 'reseaux sociaux'},
        ),
        migrations.AlterModelOptions(
            name='siteinfo',
            options={'verbose_name': 'site infos', 'verbose_name_plural': 'site infos'},
        ),
        migrations.AddField(
            model_name='presentation',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='titre',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='map_url',
            field=models.TextField(null=True),
        ),
    ]
