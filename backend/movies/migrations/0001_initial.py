# Generated by Django 3.2 on 2023-05-25 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_path', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('released_date', models.DateField()),
                ('popularity', models.FloatField()),
                ('vote_avg', models.FloatField()),
                ('overview', models.TextField()),
                ('backdrop_path', models.CharField(max_length=300, null=True)),
                ('video_path', models.CharField(max_length=300, null=True)),
                ('poster_path', models.CharField(max_length=300)),
                ('actors', models.ManyToManyField(related_name='starred_movies', to='movies.Actor')),
                ('genres', models.ManyToManyField(related_name='movie_genres', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Recommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creteria', models.CharField(max_length=50)),
                ('movielist', models.ManyToManyField(related_name='movie_recommendedlists', to='movies.Movie')),
            ],
        ),
    ]
