# Generated by Django 4.2.4 on 2023-08-29 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0008_alternativa_pontuacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alternativa',
            name='pontuacao',
        ),
    ]
