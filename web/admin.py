from django.contrib import admin

# Register your models here.

from .models import Store, Review, Subject, PreSurvey, Decision, PostSurvey

admin.site.register(Store)
admin.site.register(Review)
admin.site.register(Subject)
admin.site.register(PreSurvey)
admin.site.register(Decision)
admin.site.register(PostSurvey)

# //www.cnblogs.com/linxiyue/archive/2014/11/04/4075048.html