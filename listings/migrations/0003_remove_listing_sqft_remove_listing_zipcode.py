# Generated by Django 4.2.2 on 2023-07-06 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_state_listing_county'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='sqft',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='zipcode',
        ),
    ]
