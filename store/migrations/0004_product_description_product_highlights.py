# Generated by Django 5.1.4 on 2024-12-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='highlights',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
