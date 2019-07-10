# Generated by Django 2.0.6 on 2018-07-06 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0009_bidding_c_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='c_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bidding',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_id', to='tender.company'),
        ),
    ]
