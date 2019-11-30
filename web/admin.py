from django.contrib import admin

admin.site.site_header = '实验管理系统'
admin.site.site_title = '实验管理系统'
# Register your models here.

from .models import Store, Review, Subject, Survey, Decision, Question, Option, Choice, Log

admin.site.register(Store)
admin.site.register(Review)
admin.site.register(Subject)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Choice)
admin.site.register(Decision)
admin.site.register(Log)

# //www.cnblogs.com/linxiyue/archive/2014/11/04/4075048.html