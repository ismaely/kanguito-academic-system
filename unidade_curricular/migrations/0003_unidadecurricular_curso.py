# Generated by Django 3.2.4 on 2022-01-04 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unidade_curricular', '0002_unidadecurricular_carga_horaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadeCurricular_Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.ano')),
                ('tremestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.tremestre')),
                ('unidade_curricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='unidade_curricular.unidadecurricular')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='curso.curso')),
                ('ano_academico', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
