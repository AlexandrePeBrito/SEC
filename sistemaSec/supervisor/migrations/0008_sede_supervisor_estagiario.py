# Generated by Django 4.2.1 on 2023-06-04 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaSec_sede', '0006_remove_sede_id_nte_sede'),
        ('estagiario', '0019_delete_sede_supervisor_estagiario'),
        ('supervisor', '0007_remove_supervisor_sede_supervisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sede_Supervisor_Estagiario',
            fields=[
                ('SSES_id', models.AutoField(primary_key=True, serialize=False)),
                ('SSES_id_estagiario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SSES_id_estagiario', to='estagiario.estagiario')),
                ('SSES_id_sede', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SSES_id_sede', to='sistemaSec_sede.sede')),
                ('SSES_id_supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SSES_id_supervisor', to='supervisor.supervisor')),
            ],
            options={
                'db_table': 'SSES_sede_supervisor_estagiario',
            },
        ),
    ]
