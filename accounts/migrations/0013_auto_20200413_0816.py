# Generated by Django 3.0 on 2020-04-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200413_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_out',
            field=models.DateField(),
        ),
    ]
