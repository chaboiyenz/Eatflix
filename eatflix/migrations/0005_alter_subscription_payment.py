# Generated by Django 4.2.7 on 2024-01-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatflix', '0004_delete_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='payment',
            field=models.CharField(choices=[('Gcash', 'Gcash'), ('Paymaya', 'Paymaya'), ('Credit Card', 'Credit Card'), ('Debit Credit', 'Debit Card')], default='1', max_length=20),
        ),
    ]
