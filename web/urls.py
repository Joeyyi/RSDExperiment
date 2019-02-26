from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('instructions', views.insructions, name='instructions'),
  path('start', views.start, name='start'),
  path('all', views.listing, name='listing'),
  path('all/<int:id>', views.details, name='details'),
  path('survey', views.survey, name='survey'),
]