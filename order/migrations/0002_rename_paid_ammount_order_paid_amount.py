# Generated by Django 4.1.6 on 2023-02-06 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid_ammount',
            new_name='paid_amount',
        ),
    ]
