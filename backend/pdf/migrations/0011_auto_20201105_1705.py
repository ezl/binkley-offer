# Generated by Django 3.1.2 on 2020-11-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0010_auto_20201019_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='redfin_src',
            field=models.TextField(),
        ),
    ]
