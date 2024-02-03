# Generated by Django 5.0 on 2024-02-01 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eatflix', '0009_rename_date_added_food_food_date_added_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food_date_added',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='food_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='food_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='food_stocks',
            new_name='stocks',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='mov_date_added',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='mov_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='mov_genre',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='mov_length',
            new_name='length',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='mov_id',
            new_name='movie_id',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='mov_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='moviestream',
            old_name='movie_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='moviestream',
            old_name='movie_stream_date',
            new_name='stream_date',
        ),
        migrations.RenameField(
            model_name='moviestream',
            old_name='movie_stream_time',
            new_name='stream_time',
        ),
        migrations.RenameField(
            model_name='moviestream',
            old_name='movie_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='eatflix_id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='eatflix_date_subscription',
            new_name='date_subscription',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='eatflix_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='eatflix_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='eatflix_payment',
            new_name='payment',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='eatflix_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='tvs_date_added',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='tvs_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='tvs_episode',
            new_name='episode',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='tvs_genre',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='tvs_length',
            new_name='length',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='tvs_id',
            new_name='season',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='tvs_season',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='tvs_title',
            new_name='tv_id',
        ),
        migrations.RenameField(
            model_name='tvstream',
            old_name='tv_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tvstream',
            old_name='tv_stream_date',
            new_name='stream_date',
        ),
        migrations.RenameField(
            model_name='tvstream',
            old_name='tv_stream_time',
            new_name='stream_time',
        ),
        migrations.RenameField(
            model_name='tvstream',
            old_name='tv_title',
            new_name='title',
        ),
    ]