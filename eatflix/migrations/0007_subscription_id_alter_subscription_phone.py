# Generated by Django 5.0 on 2024-02-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatflix', '0006_subscription_date_alter_subscription_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='ID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
