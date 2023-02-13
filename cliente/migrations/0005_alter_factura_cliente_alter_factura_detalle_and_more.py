# Generated by Django 4.1.6 on 2023-02-13 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_rename_fecha_retiro_clienteretirado_fecha_retirado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.cliente'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='detalle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.detalle'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='tipo_pago',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.tipo_pago'),
        ),
    ]
