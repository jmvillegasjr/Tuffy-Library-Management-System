# Generated by Django 3.0 on 2020-04-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200412_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
