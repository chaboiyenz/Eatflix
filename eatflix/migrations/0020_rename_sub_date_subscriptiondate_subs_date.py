# Generated by Django 5.0 on 2024-02-01 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eatflix', '0019_remove_subscription_sub_date_subscription_sub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriptiondate',
            old_name='sub_date',
            new_name='subs_date',
        ),
    ]
