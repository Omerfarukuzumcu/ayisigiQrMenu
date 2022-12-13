# Generated by Django 3.1.5 on 2022-11-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('price', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('FırınUrunleri', 'Fırın Ürünleri'), ('AdetUrunleri', 'Adet Ürünler'), ('Borek', 'Börek'), ('Icecek', 'İçecek'), ('Kahvalt', 'Kahvaltı'), ('Sandvic', 'Sandvic'), ('Sarma', 'Sarma'), ('Tatlı', 'Tatlı'), ('SerbetliTatlı', 'Şerbetli Tatlı')], max_length=30)),
            ],
        ),
    ]