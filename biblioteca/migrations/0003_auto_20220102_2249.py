# Generated by Django 3.2.4 on 2022-01-02 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_livro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria_livro',
            options={},
        ),
        migrations.AddField(
            model_name='livro',
            name='arquivo',
            field=models.FileField(default=1, upload_to='livro/%Y/'),
            preserve_default=False,
        ),
    ]
