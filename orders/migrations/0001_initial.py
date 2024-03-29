# Generated by Django 3.1.3 on 2020-12-03 11:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NOWY', 'Nowy koszyk'), ('WYSŁANY', 'Wysłany')], default='NOWY', max_length=15)),
                ('date_placed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CartLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Ilość:')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NOWE', 'Utworzono nowe zamówienie'), ('PRZYJĘTE', 'Zamówienie przyjęte.'), ('ZREALIZOWANE', 'Zamówienie zrealizowane')], default='NOWE', max_length=15, verbose_name='Status zamówienia')),
                ('shipping_address1', models.CharField(max_length=60)),
                ('shipping_address2', models.CharField(max_length=60)),
                ('house_number', models.CharField(max_length=60)),
                ('flat_number', models.CharField(blank=True, max_length=60)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_placed', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Numer telefonu')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NOWE', 'Utworzono nowe zamówienie'), ('ZŁOŻONE', 'Zamówienie przyjęte'), ('PRZYGOTOWYWANIE', 'Zamówienie przygotowywane'), ('WYSŁANE', 'Zamówienie wysłane'), ('ANULOWANE', 'Zamówienie anulowane')], default='NOWE', max_length=15)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kolejka', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.food')),
            ],
        ),
    ]
