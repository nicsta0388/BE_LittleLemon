# Generated by Django 4.2.10 on 2024-02-22 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]