# Generated by Django 3.2.4 on 2022-01-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente_Grau_academico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('opcao', models.CharField(blank=True, max_length=160, null=True)),
            ],
        ),
    ]
