# Generated by Django 3.2.13 on 2023-05-20 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_remove_review_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewcomment',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='community.review'),
        ),
    ]
