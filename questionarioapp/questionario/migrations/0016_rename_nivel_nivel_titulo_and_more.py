# Generated by Django 4.2.4 on 2023-09-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0015_explicacao_nivel_alter_questionario_explicacao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nivel',
            old_name='nivel',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='explicacao',
            name='explicacao',
        ),
        migrations.AddField(
            model_name='explicacao',
            name='texto',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
