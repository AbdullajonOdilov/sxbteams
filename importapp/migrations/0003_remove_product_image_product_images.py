# Generated by Django 5.0.3 on 2024-06-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importapp', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Image',
        ),
        migrations.AddField(
            model_name='product',
            name='Images',
            field=models.ManyToManyField(to='importapp.product_image'),
        ),
    ]