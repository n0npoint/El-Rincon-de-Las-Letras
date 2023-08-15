# Generated by Django 4.2.4 on 2023-08-14 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recursos_humanos', '0001_initial'),
        ('finanzas', '0001_initial'),
        ('bodega', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbsalarios',
            name='id_empleado',
            field=models.ForeignKey(db_column='id_empleado', on_delete=django.db.models.deletion.DO_NOTHING, to='recursos_humanos.tbempleado'),
        ),
        migrations.AddField(
            model_name='tbpagos',
            name='id_empleado',
            field=models.ForeignKey(db_column='id_empleado', on_delete=django.db.models.deletion.DO_NOTHING, to='recursos_humanos.tbempleado'),
        ),
        migrations.AddField(
            model_name='tbpagos',
            name='id_factura_proveedor',
            field=models.ForeignKey(blank=True, db_column='id_factura_proveedor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finanzas.tbfacturaproveedor'),
        ),
        migrations.AddField(
            model_name='tbpagos',
            name='id_servicio',
            field=models.ForeignKey(blank=True, db_column='id_servicio', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finanzas.tbservicios'),
        ),
        migrations.AddField(
            model_name='tbfacturaproveedor',
            name='id_empleado',
            field=models.ForeignKey(db_column='id_empleado', on_delete=django.db.models.deletion.DO_NOTHING, to='recursos_humanos.tbempleado'),
        ),
        migrations.AddField(
            model_name='tbfacturaproveedor',
            name='id_pedido',
            field=models.ForeignKey(db_column='id_pedido', on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbpedidos'),
        ),
        migrations.AddField(
            model_name='tbfacturaproveedor',
            name='id_proveedor',
            field=models.ForeignKey(db_column='id_proveedor', on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbproveedor'),
        ),
        migrations.AddField(
            model_name='tbpagosxpedidos',
            name='id_pedido',
            field=models.ForeignKey(db_column='id_pedido', on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbpedidos'),
        ),
        migrations.AlterUniqueTogether(
            name='tbpagosxpedidos',
            unique_together={('id_pago', 'id_pedido')},
        ),
    ]
