# Generated by Django 3.1.2 on 2020-11-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0012_auto_20201105_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='agent_fax',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='agent_license',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='agent_mls',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='agent_phone',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='brokerage',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='brokerage_license',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='brokerage_mls',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.TextField(blank=True, default=''),
        ),
    ]
