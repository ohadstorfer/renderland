# Generated by Django 4.2.7 on 2023-11-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
