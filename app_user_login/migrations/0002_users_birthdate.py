# Generated by Django 2.2.4 on 2021-02-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='birthdate',
            field=models.DateField(default=1976),
            preserve_default=False,
        ),
    ]