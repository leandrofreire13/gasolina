# Generated by Django 3.2.8 on 2021-11-23 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Valores',
            new_name='Gastos',
        ),
    ]
