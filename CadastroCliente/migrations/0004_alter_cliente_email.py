# Generated by Django 4.2 on 2023-04-24 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0003_cliente_estado_civil_alter_cliente_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
