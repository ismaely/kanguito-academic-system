# Generated by Django 3.2.4 on 2022-01-17 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0003_estado_docente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoa.pessoa')),
                ('numero_docente', models.CharField(max_length=10, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='docente.categoria')),
                ('grau_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='docente.docente_grau_academico')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='docente.estado_docente')),
                ('data_registro', models.DateField(default=django.utils.timezone.now)),
                ('created', models.DateField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]