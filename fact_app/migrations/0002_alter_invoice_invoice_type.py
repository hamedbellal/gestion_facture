# Generated by Django 4.1.7 on 2023-02-23 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fact_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(choices=[('R', 'REÇU'), ('P', 'FACTURE PRO FORMA'), ('I', 'FACTURE')], max_length=1),
        ),
    ]
