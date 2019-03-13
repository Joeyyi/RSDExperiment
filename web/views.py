from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Subject, Survey, Question, Option, Store


def index(request):
  stores = Store.objects.all()
  return HttpResponse(len(stores))
  #return render(request, 'web/index.html')

def register(request):
  if request.method == 'GET':
    u = request.COOKIES.get('username')
    if not u:
      return render(request, 'web/register.html')
    else:
      user = request.COOKIES['username']
      return HttpResponseRedirect('instructions')

  if request.method == 'POST':
    u = request.POST.get('username', None)
    p = request.POST.get('password', None)
    if(True): # 验证
      res = HttpResponseRedirect('instructions')
      res.set_cookie('username',u,max_age=300)
      return res
    else:
      return HttpResponseRedirect('register')

def logout(request):
  res = HttpResponseRedirect('register')
  res.delete_cookie('username')
  return res

def insructions(request):
  return render(request, 'web/instructions.html')

def start(request):
  return render(request, 'web/start.html')

def all(request):
  import json
  with open("list.json",'r') as load_f:
    list_dict = json.load(load_f)
  context = {'stores': list_dict[:15]}
  return render(request, 'web/all.html', context)

def details(request):
  # import json
  # with open("list.json",'r') as load_f:
  #   list_dict = json.load(load_f)
  #   for(store in list_dict[16:]):
  #     if(store.store_id)
  # context = {'stores': list_dict[:15]}
  # return render(request, 'web/detail.html')
  return render(request, 'web/start.html')

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


