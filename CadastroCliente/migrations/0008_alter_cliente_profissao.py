# Generated by Django 4.2 on 2023-04-24 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0007_alter_profissao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Profissao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profissão', to='CadastroCliente.profissao'),
        ),
    ]
