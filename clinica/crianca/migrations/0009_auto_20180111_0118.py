# Generated by Django 2.0 on 2018-01-11 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crianca', '0008_auto_20180111_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crianca',
            name='data_cadastro',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='numero_pessoas_casa',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
