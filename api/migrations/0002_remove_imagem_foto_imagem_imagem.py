# Generated by Django 4.0.4 on 2022-05-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagem',
            name='foto',
        ),
        migrations.AddField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(default='placeholder.jpg', upload_to=''),
        ),
    ]
