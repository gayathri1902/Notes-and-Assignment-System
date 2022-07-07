# Generated by Django 3.2 on 2021-05-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0008_alter_signup_table_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('coursecode', models.CharField(max_length=20)),
                ('registration', models.CharField(default=123, max_length=100)),
                ('classnumber', models.CharField(max_length=20)),
                ('pwd', models.CharField(default=123, max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='signup_table',
            old_name='rpwd',
            new_name='pwd',
        ),
    ]