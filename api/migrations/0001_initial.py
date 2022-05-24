# Generated by Django 4.0.4 on 2022-05-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=30)),
                ('ambiente', models.CharField(max_length=30)),
                ('itens', models.CharField(max_length=10000)),
                ('foto', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
    ]
