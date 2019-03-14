from django.db import models

# Create your models here.

class Store(models.Model):
  store_id= models.CharField(max_length=50,unique=True,primary_key=True,verbose_name='商户id')
  store_name= models.CharField(max_length=50,verbose_name='商户id',default='点评商户')
  store_stars= models.CharField(max_length=5,verbose_name='商户评分',default='4.5')
  store_avg= models.IntegerField(verbose_name='商户人均',default=100)
  store_addr= models.CharField(max_length=50,verbose_name='商户地址',default='暂无地址')
  store_num_review = models.IntegerField(verbose_name='商户点评数',default=50)
  store_rec= models.CharField(max_length=50,verbose_name='商户推荐菜',default='暂无推荐菜')
  store_region= models.CharField(max_length=20,verbose_name='商户地区',default='暂无地区')
  store_category= models.CharField(max_length=20,verbose_name='商户分类',default='暂无分类')
  store_flavor= models.CharField(max_length=5,verbose_name='商户口味分',default='8.5')
  store_envir = models.CharField(max_length=5,verbose_name='商户环境分',default='8.5')
  store_service = models.CharField(max_length=5,verbose_name='商户服务分',default='8.5')
  store_phone = models.CharField(max_length=30,verbose_name='商户电话',default='暂无电话')

class Review(models.Model):
  review_id = models.AutoField(primary_key=True)
  review_author = models.CharField(max_length=50,verbose_name='点评用户',default='匿名用户')
  review_author_lv = models.IntegerField(verbose_name='点评id',default='点评用户等级')
  review_store = models.ForeignKey(Store,to_field='store_id',on_delete=models.CASCADE,verbose_name='点评商户')
  review_stars = models.IntegerField(verbose_name='点评评分',default=5)
  review_flavor = models.IntegerField(verbose_name='点评口味分',default=5)
  review_envir = models.IntegerField(verbose_name='点评环境分',default=5)
  review_service = models.IntegerField(verbose_name='点评服务分',default=5)
  review_date = models.CharField(max_length=500,verbose_name='点评日期',default='2019-01-01')
  review_likes = models.IntegerField(verbose_name='点评点赞数',default=7)
  review_rec = models.CharField(max_length=50,verbose_name='点评推荐菜',default='')

class Subject(models.Model):
  sub_id = models.AutoField(primary_key=True)
  sub_name = models.CharField(max_length=20,verbose_name='被试姓名')
  sub_email = models.CharField(max_length=50,verbose_name='被试邮箱')
  sub_created = models.DateTimeField(verbose_name='被试注册时间')
  def __str__(self):
    return self.sub_name

class PreSurvey(models.Model):
  AGE_CHOICES = (
    ('1','18岁以下'),
    ('2','18-25岁'),
    ('3','26-35岁'),
    ('4','35岁以上')
  )
  GENDER_CHOICES = (
    ('M', '男'),
    ('F', '女'),
  )
  sub_id = models.OneToOneField(Subject,on_delete=models.CASCADE,verbose_name='基本信息被试id',primary_key=True)
  sub_age = models.CharField(max_length=1,choices=AGE_CHOICES,verbose_name='被试年龄')
  sub_gender = models.CharField(max_length=1,choices=GENDER_CHOICES,verbose_name='被试性别')
  sub_frequency = models.CharField(max_length=1,verbose_name='被试网站使用频率')
  sub_attitude = models.CharField(max_length=1,verbose_name='被试对评论参考程度')

class Decision(models.Model):
  dec_id = models.AutoField(primary_key=True)
  dec_store = models.ForeignKey(Store,to_field='store_id',on_delete=models.CASCADE,verbose_name='点评商户')
  dec_sub = models.OneToOneField(Subject,on_delete=models.CASCADE,verbose_name='决策被试id')
  dec_time = models.IntegerField(verbose_name='决策时间')

class PostSurvey(models.Model):
  sur_id = models.AutoField(primary_key=True)
  sur_sub = models.ForeignKey(Subject,to_field='sub_id',on_delete=models.CASCADE,verbose_name='问卷被试id')
  sub_choice = models.CharField(max_length=50,verbose_name='问卷答案')

# class Subject(models.Model):
#   name = models.CharField(max_length=20,verbose_name='被试姓名')
#   date_created = models.DateTimeField(verbose_name='被试注册时间')
#   age = models.IntegerField(verbose_name='被试年龄')
#   email = models.CharField(max_length=50,verbose_name='被试邮箱')
#   gender = models.IntegerField(default=1,verbose_name='被试性别')
#   def __str__(self):
#     return self.name

# class Survey(models.Model):
#   title = models.CharField(max_length=50,verbose_name='问卷名称')
#   description = models.CharField(max_length=1000,verbose_name='问卷描述')
#   def __str__(self):
#     return self.title

# class Question(models.Model):
#   caption = models.CharField(max_length=500,verbose_name='题目描述')
#   type_question = models.IntegerField(default=1,verbose_name='问题类型')
#   survey = models.models.ForeignKey(Survey,on_delete=models.CASCADE,verbose_name='所属问卷')
#   def __str__(self):
#     return self.caption

# class Option(models.Model):
#   question = models.models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name='所属问题')
#   description = models.CharField(max_length=50,verbose_name='选项描述')
#   value = models.IntegerField(verbose_name='选项分值')
#   def __str__(self):
#     return self.description

# class Choice(models.Model):
#   subject = models.models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='所属被试')
#   question = models.models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name='所属问题')
#   option = models.models.ForeignKey(Option,on_delete=models.CASCADE,verbose_name='回答')
#   def __str__(self):
#     return '%d - %d - %d' % (self.subject.id,self.question.id,self.option.id)

# https://blog.csdn.net/myhuashengmi/article/details/53106301