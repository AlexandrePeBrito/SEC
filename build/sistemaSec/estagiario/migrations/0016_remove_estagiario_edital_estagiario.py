# Generated by Django 4.2.1 on 2023-06-03 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estagiario', '0015_alter_estagiario_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estagiario',
            name='edital_estagiario',
        ),
    ]
