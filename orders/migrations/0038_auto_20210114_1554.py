# Generated by Django 3.1.3 on 2021-01-14 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_auto_20210105_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address1',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address2',
            new_name='street',
        ),
    ]