# Generated by Django 4.1.6 on 2023-02-04 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_thumbnail_product_thumbbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='thumbbnail',
            new_name='thumbnail',
        ),
    ]
