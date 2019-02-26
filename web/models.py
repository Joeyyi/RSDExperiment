from django.db import models

# Create your models here.

class Subject(models.Model):
  name = models.CharField(max_length=20, verbose_name='被试姓名')
  date_created = models.DateTimeField(verbose_name='被试注册时间')
  age = models.IntegerField(verbose_name='被试年龄')
  email = models.CharField(max_length=50, verbose_name='被试邮箱')
  gender = models.IntegerField(default=1, verbose_name='被试性别')
  def __str__(self):
    return self.name

class Survey(models.Model):
  title = models.CharField(max_length=50, verbose_name='问卷名称')
  description = models.CharField(max_length=1000, verbose_name='问卷描述')
  def __str__(self):
    return self.title

class Question(models.Model):
  caption = models.CharField(max_length=500, verbose_name='题目描述')
  types = (
    (1, '单选'),
    (2, '多选')
  )
  type_question = models.IntegerField(choices=types, verbose_name='问题类型')
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='所属问卷')
  def __str__(self):
    return self.caption

class Option(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='所属问题')
  description = models.CharField(max_length=50, verbose_name='选项描述')
  value = models.IntegerField(verbose_name='选项分值')
  def __str__(self):
    return self.description

class Choice(models.Model):
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='所属被试')
  question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='所属问题')
  option = models.ForeignKey(Option, on_delete=models.CASCADE, verbose_name='回答')
  def __str__(self):
    return '%d - %d - %d' % (self.subject.id, self.question.id, self.option.id)

# https://blog.csdn.net/myhuashengmi/article/details/53106301