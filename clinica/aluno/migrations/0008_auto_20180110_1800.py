# Generated by Django 2.0 on 2018-01-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0007_auto_20180110_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
