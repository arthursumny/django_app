# Generated by Django 4.2.4 on 2023-08-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0010_alternativa_pontuacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sommatory', models.IntegerField()),
                ('explanation', models.CharField(max_length=255)),
            ],
        ),
    ]