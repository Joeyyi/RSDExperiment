# Generated by Django 2.1.5 on 2019-03-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20190319_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='decision',
            name='dec_time',
        ),
        migrations.AddField(
            model_name='decision',
            name='dec_duration',
            field=models.FloatField(default=0, verbose_name='决策时间'),
        ),
    ]