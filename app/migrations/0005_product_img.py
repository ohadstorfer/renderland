# Generated by Django 4.2.7 on 2023-11-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_description_category_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='../static/images/default.png', upload_to=''),
        ),
    ]
