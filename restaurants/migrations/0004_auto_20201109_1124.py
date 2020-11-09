# Generated by Django 3.1.3 on 2020-11-09 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20201106_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='c_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='f_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='f_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='f_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='f_restaurant',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='r_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='r_name',
            new_name='name',
        ),
    ]
