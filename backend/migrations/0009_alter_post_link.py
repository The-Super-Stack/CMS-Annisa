# Generated by Django 3.2.7 on 2021-10-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_profile_nick_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
    ]
