# Generated by Django 5.0.3 on 2024-03-25 20:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratica', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ousuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('genero', models.CharField(choices=[('T', 'Transgênero'), ('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Não-binário')], max_length=1)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('endereco', models.CharField(max_length=100)),
                ('renda_mensal', models.FloatField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pratica.cidade')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pratica.estado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('exerce', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pratica.profissao')),
            ],
        ),
    ]
