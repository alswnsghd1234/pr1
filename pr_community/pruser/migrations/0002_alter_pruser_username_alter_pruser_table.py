# Generated by Django 4.0.1 on 2022-01-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruser',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
        migrations.AlterModelTable(
            name='pruser',
            table='pruser_pruser',
        ),
    ]
