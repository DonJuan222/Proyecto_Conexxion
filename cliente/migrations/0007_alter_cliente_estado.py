# Generated by Django 4.1.7 on 2023-03-13 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_remove_cliente_mensualidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(blank=True, choices=[('Activos', 'Activos'), ('Suspendidos', 'Suspendidos'), ('Retiros', 'Retiros')], max_length=13, null=True),
        ),
    ]
