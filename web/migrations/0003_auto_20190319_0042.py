# Generated by Django 2.1.5 on 2019-03-18 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190317_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sub_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='被试注册时间'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_group',
            field=models.CharField(choices=[('0', 'test'), ('1', '1组'), ('2', '2组'), ('3', '3组'), ('4', '4组'), ('4', '5组'), ('4', '6组'), ('4', '7组')], max_length=1, verbose_name='被试组别'),
        ),
    ]
