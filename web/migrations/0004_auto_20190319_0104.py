# Generated by Django 2.1.5 on 2019-03-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190319_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sub_number',
            field=models.CharField(max_length=20, verbose_name='被试学号'),
        ),
    ]