# Generated by Django 3.1.3 on 2020-12-27 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_orderproduct_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
