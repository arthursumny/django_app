# Generated by Django 4.2.4 on 2023-08-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0007_remove_alternativa_pontuacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternativa',
            name='pontuacao',
            field=models.IntegerField(default=0),
        ),
    ]