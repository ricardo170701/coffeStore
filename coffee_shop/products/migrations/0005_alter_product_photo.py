# Generated by Django 5.1.2 on 2024-11-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='/A_small_cup_of_coffee.JPG', upload_to='', verbose_name='foto'),
        ),
    ]
