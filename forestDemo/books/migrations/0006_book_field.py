# Generated by Django 3.2.4 on 2022-04-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='field',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=1000),
        ),
    ]