# Generated by Django 5.1.2 on 2024-10-23 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='date_ordered',
        ),
    ]
