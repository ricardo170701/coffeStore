# Generated by Django 5.1.2 on 2024-10-28 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create',
            field=models.DateField(auto_now=True),
        ),
    ]