# Generated by Django 4.0.4 on 2022-05-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_imagem_foto_imagem_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'nao feito'), (1, 'feito')], default='1'),
            preserve_default=False,
        ),
    ]