# Generated by Django 4.1.5 on 2023-05-30 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0006_remove_venda_moto_motovenda_carrinho"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carrinho",
            name="quantidade",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="moto",
            name="quantidade",
            field=models.IntegerField(default=1),
        ),
    ]
