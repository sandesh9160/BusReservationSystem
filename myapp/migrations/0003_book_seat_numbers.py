# Generated by Django 4.0.3 on 2024-08-26 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_book_options_alter_bus_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='seat_numbers',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
