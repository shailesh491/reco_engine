# Generated by Django 2.1.2 on 2018-10-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0005_auto_20181020_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
