from django.contrib import admin

# Register your models here.

from .models import Store, Review, Subject, Survey, Decision, Question, Option, Choice

admin.site.register(Store)
admin.site.register(Review)
admin.site.register(Subject)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Choice)
admin.site.register(Decision)

# //www.cnblogs.com/linxiyue/archive/2014/11/04/4075048.html