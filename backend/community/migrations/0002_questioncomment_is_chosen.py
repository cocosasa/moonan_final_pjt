# Generated by Django 3.2.13 on 2023-05-25 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioncomment',
            name='is_chosen',
            field=models.BooleanField(default=False),
        ),
    ]
