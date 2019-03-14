# Generated by Django 2.1.5 on 2019-03-14 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('dec_id', models.AutoField(primary_key=True, serialize=False)),
                ('dec_time', models.IntegerField(verbose_name='决策时间')),
            ],
        ),
        migrations.CreateModel(
            name='PostSurvey',
            fields=[
                ('sur_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_choice', models.CharField(max_length=50, verbose_name='问卷答案')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_author', models.CharField(default='匿名用户', max_length=50, verbose_name='点评用户')),
                ('review_author_lv', models.IntegerField(default='点评用户等级', verbose_name='点评id')),
                ('review_stars', models.IntegerField(default=5, verbose_name='点评评分')),
                ('review_flavor', models.IntegerField(default=5, verbose_name='点评口味分')),
                ('review_envir', models.IntegerField(default=5, verbose_name='点评环境分')),
                ('review_service', models.IntegerField(default=5, verbose_name='点评服务分')),
                ('review_date', models.CharField(default='2019-01-01', max_length=500, verbose_name='点评日期')),
                ('review_likes', models.IntegerField(default=7, verbose_name='点评点赞数')),
                ('review_rec', models.CharField(default='', max_length=50, verbose_name='点评推荐菜')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='商户id')),
                ('store_name', models.CharField(default='点评商户', max_length=50, verbose_name='商户id')),
                ('store_stars', models.CharField(default='4.5', max_length=5, verbose_name='商户评分')),
                ('store_avg', models.IntegerField(default=100, verbose_name='商户人均')),
                ('store_addr', models.CharField(default='暂无地址', max_length=50, verbose_name='商户地址')),
                ('store_num_review', models.IntegerField(default=50, verbose_name='商户点评数')),
                ('store_rec', models.CharField(default='暂无推荐菜', max_length=50, verbose_name='商户推荐菜')),
                ('store_region', models.CharField(default='暂无地区', max_length=20, verbose_name='商户地区')),
                ('store_category', models.CharField(default='暂无分类', max_length=20, verbose_name='商户分类')),
                ('store_flavor', models.CharField(default='8.5', max_length=5, verbose_name='商户口味分')),
                ('store_envir', models.CharField(default='8.5', max_length=5, verbose_name='商户环境分')),
                ('store_service', models.CharField(default='8.5', max_length=5, verbose_name='商户服务分')),
                ('store_phone', models.CharField(default='暂无电话', max_length=30, verbose_name='商户电话')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=20, verbose_name='被试姓名')),
                ('sub_email', models.CharField(max_length=50, verbose_name='被试邮箱')),
                ('sub_created', models.DateTimeField(verbose_name='被试注册时间')),
            ],
        ),
        migrations.CreateModel(
            name='PreSurvey',
            fields=[
                ('sub_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.Subject', verbose_name='基本信息被试id')),
                ('sub_age', models.CharField(choices=[('1', '18岁以下'), ('2', '18-25岁'), ('3', '26-35岁'), ('4', '35岁以上')], max_length=1, verbose_name='被试年龄')),
                ('sub_gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=1, verbose_name='被试性别')),
                ('sub_frequency', models.CharField(max_length=1, verbose_name='被试网站使用频率')),
                ('sub_attitude', models.CharField(max_length=1, verbose_name='被试对评论参考程度')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='review_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Store', verbose_name='点评商户'),
        ),
        migrations.AddField(
            model_name='postsurvey',
            name='sur_sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Subject', verbose_name='问卷被试id'),
        ),
        migrations.AddField(
            model_name='decision',
            name='dec_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Store', verbose_name='点评商户'),
        ),
        migrations.AddField(
            model_name='decision',
            name='dec_sub',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.Subject', verbose_name='决策被试id'),
        ),
    ]
