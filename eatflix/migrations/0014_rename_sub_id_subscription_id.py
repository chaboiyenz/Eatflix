# Generated by Django 5.0 on 2024-02-01 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eatflix', '0013_rename_id_subscription_sub_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='sub_id',
            new_name='ID',
        ),
    ]