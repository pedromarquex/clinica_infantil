# Generated by Django 2.1.2 on 2018-10-19 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, null=True)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('sexo', models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino')], max_length=10, null=True)),
                ('data_nascimento', models.DateField(null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='perfil')),
                ('matricula', models.CharField(max_length=11, null=True)),
                ('telefone', models.CharField(max_length=12, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('aprovado', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
