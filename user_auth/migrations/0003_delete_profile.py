# Generated by Django 3.2.16 on 2022-10-06 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
