# Generated by Django 4.2.3 on 2023-07-08 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_conta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='valor',
            field=models.FloatField(),
        ),
    ]
