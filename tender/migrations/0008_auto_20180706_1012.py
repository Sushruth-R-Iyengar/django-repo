# Generated by Django 2.0.6 on 2018-07-06 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0007_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='company',
        ),
    ]
