# Generated by Django 5.0 on 2024-02-01 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eatflix', '0012_rename_name_feedback_feeds_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='ID',
            new_name='sub_id',
        ),
    ]
