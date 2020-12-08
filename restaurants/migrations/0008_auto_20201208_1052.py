# Generated by Django 3.1.3 on 2020-12-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20201207_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodimage',
            options={'verbose_name': 'Obraz produktu', 'verbose_name_plural': 'Obrazy produktu'},
        ),
        migrations.AddField(
            model_name='restaurant',
            name='city',
            field=models.CharField(default='Kraków', max_length=150, verbose_name='Miasto:'),
        ),
    ]