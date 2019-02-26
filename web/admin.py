from django.contrib import admin

# Register your models here.

from .models import Subject, Survey, Question, Option

admin.site.register(Subject)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Option)

# //www.cnblogs.com/linxiyue/archive/2014/11/04/4075048.html