# Generated by Django 4.2.4 on 2023-08-14 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recursos_humanos', '0001_initial'),
        ('bodega', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbpedidos',
            name='id_empleado',
            field=models.ForeignKey(db_column='id_empleado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='recursos_humanos.tbempleado'),
        ),
        migrations.AddField(
            model_name='tbpedidos',
            name='id_proveedor',
            field=models.ForeignKey(db_column='id_proveedor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbproveedor'),
        ),
        migrations.AddField(
            model_name='tblibros',
            name='id_autor',
            field=models.ForeignKey(db_column='id_autor', on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbautor', verbose_name='ID Autor'),
        ),
        migrations.AddField(
            model_name='tblibros',
            name='id_editorial',
            field=models.ForeignKey(db_column='id_editorial', on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbeditorial', verbose_name='ID Editorial'),
        ),
        migrations.AddField(
            model_name='tblibroxproveedor',
            name='id_proveedor',
            field=models.ForeignKey(db_column='id_proveedor', on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbproveedor'),
        ),
        migrations.AddField(
            model_name='tblibroxpedido',
            name='id_pedido',
            field=models.ForeignKey(db_column='id_pedido', on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbpedidos'),
        ),
        migrations.AlterUniqueTogether(
            name='tblibros',
            unique_together={('id_libro', 'isbn')},
        ),
        migrations.AddField(
            model_name='tbeditorialxproveedor',
            name='id_editorial',
            field=models.ForeignKey(db_column='id_editorial', on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbeditorial'),
        ),
        migrations.AddField(
            model_name='tbcategoriaxlibro',
            name='id_categoria',
            field=models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.DO_NOTHING, to='bodega.tbcategoria'),
        ),
        migrations.AlterUniqueTogether(
            name='tblibroxproveedor',
            unique_together={('isbn', 'id_proveedor')},
        ),
        migrations.AlterUniqueTogether(
            name='tblibroxpedido',
            unique_together={('isbn', 'id_pedido')},
        ),
    ]