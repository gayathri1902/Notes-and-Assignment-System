# Generated by Django 3.2.2 on 2021-05-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0009_auto_20210520_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_table',
            name='pwd',
            field=models.CharField(default=456, max_length=100),
        ),
    ]