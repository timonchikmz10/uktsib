# Generated by Django 4.1.1 on 2022-09-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_intopost_allpost_alter_intopost_sources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', help_text='max length 200s', max_length=200, unique=True),
        ),
    ]
