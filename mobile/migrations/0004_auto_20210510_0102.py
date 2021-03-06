# Generated by Django 3.2 on 2021-05-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price_total',
            field=models.PositiveBigIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
