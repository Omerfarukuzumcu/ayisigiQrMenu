# Generated by Django 3.1.5 on 2022-11-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20221130_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]