# Generated by Django 5.0.2 on 2024-04-01 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_postphoto_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postphoto',
            options={'verbose_name': 'Картинки', 'verbose_name_plural': 'Картинки'},
        ),
    ]
