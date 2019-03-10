from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Subject, Survey, Question, Option

def index(request):

  return render(request, 'web/index.html')

def insructions(request):
  return HttpResponse("实验指导")

def start(request):
  return HttpResponse("点评网站首页")

def listing(request):
  import json
  with open("list.json",'r') as load_f:
    list_dict = json.load(load_f)
  context = {'stores': list_dict[:15]}
  return render(request, 'web/list.html', context)

def details(request):
  import json
  with open("list.json",'r') as load_f:
    list_dict = json.load(load_f)
    # for(store in list_dict[16:]):
    #   if(store.store)
  context = {'stores': list_dict[:15]}
  return render(request, 'web/detail.html')

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


