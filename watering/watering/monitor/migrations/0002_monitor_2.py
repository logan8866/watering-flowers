# Generated by Django 3.0.8 on 2020-07-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField(verbose_name='year')),
                ('month', models.SmallIntegerField(verbose_name='month')),
                ('day', models.SmallIntegerField(verbose_name='day')),
                ('hour', models.SmallIntegerField(verbose_name='hour')),
                ('minute', models.SmallIntegerField(verbose_name='minute')),
                ('second', models.SmallIntegerField(verbose_name='second')),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='humidity')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='temperature')),
            ],
        ),
    ]
