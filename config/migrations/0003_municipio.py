# Generated by Django 3.2.4 on 2021-12-25 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_grau_academico_tremestre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.provincia')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(blank=True, default=' ', max_length=60, null=True)),
            ],
        ),
    ]
