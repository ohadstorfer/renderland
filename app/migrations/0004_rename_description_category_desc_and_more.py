# Generated by Django 4.2.7 on 2023-11-09 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='description',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='desc',
        ),
    ]