from django.urls import path
from . import views

urlpatterns = [
  path('index', views.index, name='index'),
  path('register', views.register, name='register'),
  path('logout', views.logout, name='logout'),
  path('instructions', views.insructions, name='instructions'),
  path('start', views.start, name='start'),
  path('all', views.all, name='all'),
  path('all/<int:id>', views.details, name='details'),
  path('survey', views.survey, name='survey'),
  path('goodbye', views.goodbye, name='goodbye'),
]