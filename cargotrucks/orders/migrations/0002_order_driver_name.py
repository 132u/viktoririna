# Generated by Django 3.2.4 on 2021-06-22 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='driver_name',
            field=models.CharField(default='driver', max_length=255),
            preserve_default=False,
        ),
    ]