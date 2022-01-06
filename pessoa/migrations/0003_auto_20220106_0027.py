# Generated by Django 3.2.4 on 2022-01-06 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_ano'),
        ('pessoa', '0002_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='genero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.genero'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.municipio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.provincia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
