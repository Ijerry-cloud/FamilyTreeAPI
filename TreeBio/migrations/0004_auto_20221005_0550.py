# Generated by Django 3.2 on 2022-10-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreeBio', '0003_auto_20211212_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='treebio2',
            name='bio2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='treebio2',
            name='bio3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='treebio2',
            name='bio4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='treebio2',
            name='bio5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='treebio2',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='main_events/%Y/%m/%d/'),
        ),
    ]