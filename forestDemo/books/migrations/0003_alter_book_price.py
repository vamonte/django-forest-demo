# Generated by Django 3.2.12 on 2022-03-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(choices=[(1.0, 1.0), (2.0, 2.0)], decimal_places=2, default=1.0, max_digits=5),
        ),
    ]