# Generated by Django 3.0 on 2020-04-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200413_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_in',
            field=models.DateTimeField(),
        ),
    ]
