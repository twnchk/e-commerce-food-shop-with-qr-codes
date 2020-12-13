# Generated by Django 3.1.3 on 2020-12-13 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0034_auto_20201209_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.order'),
        ),
    ]
