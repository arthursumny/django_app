# Generated by Django 4.2.4 on 2023-09-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0022_alternativa_pontuacao_delete_pontuacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario',
            name='imagem',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media'),
        ),
    ]
