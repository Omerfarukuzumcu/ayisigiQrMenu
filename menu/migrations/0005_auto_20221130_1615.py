# Generated by Django 3.1.5 on 2022-11-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20221130_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]