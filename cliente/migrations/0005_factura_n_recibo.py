# Generated by Django 4.1.7 on 2023-03-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_alter_factura_tipo_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='n_recibo',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]