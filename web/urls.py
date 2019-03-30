from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('index', views.index, name='index'),
  path('register', views.register, name='register'),
  path('logout', views.logout, name='logout'),
  path('log', views.log, name='log'),
  path('instructions', views.insructions, name='instructions'),
  path('start', views.start, name='start'),
  path('all', views.all, name='all'),
  path('all/<int:store_id>', views.details, name='details'),
  path('survey', views.survey, name='survey'),
  path('goodbye', views.goodbye, name='goodbye'),
]