# Generated by Django 4.2 on 2023-04-25 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0010_remove_cliente_telefone_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
    ]
