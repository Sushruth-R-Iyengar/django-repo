# Generated by Django 2.0.6 on 2018-07-06 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0006_auto_20180706_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=30, null=True)),
                ('c_reg_no', models.CharField(max_length=12, unique=True)),
            ],
        ),
    ]
