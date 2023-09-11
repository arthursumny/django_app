# Generated by Django 4.2.4 on 2023-09-11 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0020_rename_titulo1_nivel_titulo_explicacao_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alternativa',
            name='pontuacao',
        ),
        migrations.CreateModel(
            name='Pontuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontuacao', models.IntegerField(default=0)),
                ('alternativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionario.alternativa')),
            ],
        ),
    ]
