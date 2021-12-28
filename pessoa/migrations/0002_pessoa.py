# Generated by Django 3.2.4 on 2021-12-25 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('nome_pai', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('nome_mae', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('genero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.genero')),
                ('data_nascimento', models.CharField(max_length=20)),
                ('ndi', models.CharField(max_length=40)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.documento_identificacao')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.estado_civil')),
                ('residencia', models.CharField(blank=True, max_length=100, null=True)),
                ('telefone', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=190, null=True)),
                ('dificiencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoa.dificiencia')),
                ('tipo_Dificiencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoa.tipo_dificiencia')),
                ('provincia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, parent_link=True, to='config.provincia')),
                ('municipio', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, parent_link=True, to='config.municipio')),
                ('nacionalidade', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='config.pais')),
                ('foto', models.ImageField(blank=True, default='user.jpg', null=True, upload_to='fotos/')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]