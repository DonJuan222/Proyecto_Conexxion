# Generated by Django 4.1.7 on 2023-03-12 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_facturaretirada_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='tipo_pago',
            field=models.CharField(blank=True, choices=[('#Recibo', '#Recibo'), ('Bancos', 'Bancos'), ('Acertemos', 'Acertemos'), ('Nequi', 'Nequi')], max_length=15, null=True),
        ),
    ]