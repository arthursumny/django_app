# Generated by Django 4.2.4 on 2023-08-31 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0013_explicacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='explicacao',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='Explicacao',
        ),
    ]
