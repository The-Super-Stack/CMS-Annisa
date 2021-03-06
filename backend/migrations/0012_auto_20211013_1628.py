# Generated by Django 3.2.7 on 2021-10-13 09:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='desc',
            field=ckeditor.fields.RichTextField(verbose_name='Deskripsi Singkat Tentang Kamu : '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_media',
            field=models.ManyToManyField(blank=True, to='backend.SocialMedia', verbose_name='Shared Social Media : '),
        ),
    ]
