# Generated by Django 2.2.4 on 2021-02-25 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user_login', '0003_auto_20210225_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='birthdate',
        ),
    ]
