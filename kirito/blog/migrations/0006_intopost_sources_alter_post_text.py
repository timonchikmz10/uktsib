# Generated by Django 4.1.1 on 2022-09-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_time_to_reat_intopost_time_to_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='intopost',
            name='sources',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=3000),
        ),
    ]
