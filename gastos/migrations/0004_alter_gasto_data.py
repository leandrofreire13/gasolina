# Generated by Django 3.2.8 on 2021-11-23 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0003_rename_gastos_gasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
