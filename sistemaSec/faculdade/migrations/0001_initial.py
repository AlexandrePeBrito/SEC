# Generated by Django 3.2.11 on 2022-06-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculdade',
            fields=[
                ('id_faculdade', models.AutoField(primary_key=True, serialize=False)),
                ('nome_faculdade', models.CharField(max_length=200)),
                ('cnpj_faculdade', models.CharField(max_length=14)),
                ('nome_direitor_faculdade', models.CharField(max_length=100)),
                ('telefone_faculdade', models.CharField(max_length=13)),
                ('campus_faculdade', models.CharField(max_length=50)),
            ],
        ),
    ]
