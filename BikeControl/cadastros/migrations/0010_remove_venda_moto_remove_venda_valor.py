# Generated by Django 4.1.5 on 2023-06-27 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0009_venda_moto_venda_valor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="venda",
            name="moto",
        ),
        migrations.RemoveField(
            model_name="venda",
            name="valor",
        ),
    ]
