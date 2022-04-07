# Generated by Django 3.2.4 on 2022-04-07 14:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(choices=[(1.0, 1.0), (2.0, 2.0), (10.01, 10.01)], decimal_places=2, default=1.0, max_digits=5, validators=[django.core.validators.MaxValueValidator(10.01)]),
        ),
    ]
