# Generated by Django 3.1.7 on 2021-04-13 12:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20210412_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='master_advert_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя мастера из рекламы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='working_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 13, 59, 43, 93132, tzinfo=utc), verbose_name='Когда начинать работу'),
        ),
    ]
