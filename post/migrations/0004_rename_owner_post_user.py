# Generated by Django 4.1.1 on 2022-09-29 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_post_dat_post_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='user',
        ),
    ]
