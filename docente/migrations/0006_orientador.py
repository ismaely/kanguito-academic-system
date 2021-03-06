# Generated by Django 3.2.4 on 2022-02-01 12:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0005_estado_orientador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orientador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='docente.docente')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='curso.curso')),
                ('data_limite', models.DateField(default=django.utils.timezone.now)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='docente.estado_orientador')),
                ('created', models.DateField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
