# Generated by Django 3.2.11 on 2022-07-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagiario', '0010_alter_estagiario_nome_estagiario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estagiario',
            name='rg_estagiario',
            field=models.CharField(max_length=12),
        ),
    ]
