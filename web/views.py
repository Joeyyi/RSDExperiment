from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Subject, Survey, Question, Option

def index(request):

  return HttpResponse("welcome")

def insructions(request):
  return HttpResponse("实验指导")

def start(request):
  return HttpResponse("点评网站首页")

def listing(request):
  return HttpResponse("商户列表")

def details(request):
  return HttpResponse("商户详情")

def survey(request):
  survey = Survey.objects.get(id=1)
  question_list = Question.objects.filter(survey__id=1)
  for q in question_list:
    q.options = Option.objects.filter(question=q.id)
  context = {
    'survey': survey,
    'question_list': question_list
    }
  return render(request, 'web/survey.html', context)


