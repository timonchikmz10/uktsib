# Generated by Django 4.1.1 on 2022-09-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_intopost_header_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='intopost',
            name='under_article',
            field=models.CharField(default='', help_text='max length 20s', max_length=20),
        ),
    ]
