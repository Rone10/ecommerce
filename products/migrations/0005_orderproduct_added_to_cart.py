# Generated by Django 3.1.3 on 2020-12-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201217_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='added_to_cart',
            field=models.BooleanField(default=False),
        ),
    ]