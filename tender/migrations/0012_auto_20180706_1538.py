# Generated by Django 2.0.6 on 2018-07-06 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0011_auto_20180706_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bidding',
            old_name='com_id',
            new_name='c_id',
        ),
        migrations.RemoveField(
            model_name='company',
            name='c_id',
        ),
    ]
