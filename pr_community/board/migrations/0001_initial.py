# Generated by Django 4.0.1 on 2022-01-18 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pruser', '0003_alter_pruser_options_pruser_useremail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruser.pruser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '프로젝트 게시글',
                'verbose_name_plural': '프로젝트 게시글',
                'db_table': 'pr1_board',
            },
        ),
    ]
