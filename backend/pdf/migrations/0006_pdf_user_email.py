# Generated by Django 3.1.2 on 2020-10-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0005_auto_20201012_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='user_email',
            field=models.TextField(default=''),
        ),
    ]
