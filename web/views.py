from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from django import forms

from .models import Store, Review, Subject, Decision, Survey, Question, Option, Choice, Log
import random
from datetime import datetime, timedelta

# 有做form的野心

def check_login(func):
  """
  查看session值用来判断用户是否已经登录
  :param func:
  :return:
  """
  def wrapper(request,*args,**kwargs):
    if request.session.get('is_active', False):
      return func(request,*args,**kwargs)
    else:
      return HttpResponseRedirect('/exp/register?mode=error')

  return wrapper

def logger(userid,action,value=None):
  time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
  print(f'{userid}/{action}/{value}/{time}')
  s = Subject.objects.get(pk=userid)
  l = Log(subject=s, action=action, value=value, time=time)
  l.save()

def log_visit(func):
  def timed(request,*args, **kw):
    result = func(request, *args, **kw)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    logger(userid=request.session.get('id', None), action='visit', value=request.path)

    return result

  return timed

def register(request):
  if request.method == 'GET':
    # context = {
    #   'mode': request.GET.get('mode', '')
    # }
    # u = request.session.get('is_active', False)
    # if u:
    #   context.mode = 'loggedin'
    #   context.user = request.session.get('username')
    # return render(request, 'web/register.html', context=context)
    return render(request, 'web/register.html')

  if request.method == 'POST':
    u = request.POST.get('name', None)
    n = request.POST.get('number', None)
    c = request.POST.get('contact', None)
    if u: # 验证
      s = Subject(sub_name=u,sub_number=n,sub_contact=c,sub_group=random.randint(1,5))
      s.save()
      s = Subject.objects.filter(sub_number=n).order_by('-sub_created')[0]
      request.session.set_expiry(600)
      request.session['is_active'] = True
      request.session['username'] = request.POST['name']
      request.session['id'] = s.sub_id
      request.session['group'] = s.sub_group
      request.session['seed'] = random.randint(0,100)
      return HttpResponseRedirect('index')
    else:
      # return HttpResponse(u)
      return HttpResponseRedirect('register?mode=error')

def logout(request):
  request.session.flush()
  return HttpResponseRedirect('register')

@check_login
@log_visit
def index(request):
  if request.method == 'GET':
    s = Survey.objects.get(category=1)
    qlist = Question.objects.filter(survey__id=s.id).order_by('order')
    for q in qlist:
      q.options = Option.objects.filter(question=q.id)
    context = {
      'survey': s,
      'qlist': qlist
    }
    return render(request, 'web/index.html',context)
  if request.method == 'POST':
    s = Survey.objects.get(category=1)
    qlist = Question.objects.filter(survey__id=s.id).order_by('order')
    print(request.POST)
    for q in qlist:
      ans = request.POST[f"{q.id}"]
      ch = Choice(subject=Subject.objects.get(pk=request.session['id']),question=q,option=Option.objects.get(pk=ans))
      ch.save()
    return HttpResponseRedirect('instructions')

@check_login
@log_visit
def insructions(request):
  return render(request, 'web/instructions.html')

@check_login
@log_visit
def start(request):
  stores = Store.objects.all()
  return render(request, 'web/start.html', {'num':len(stores)})

@check_login
@log_visit
def all(request):
  if request.method == "GET":
    # import json
    # with open("list.json",'r') as load_f:
    #   list_dict = json.load(load_f)
    # context = {'stores': list_dict[:15], 'user': {'userid': request.session.get('id', None)}}
    stores = list(Store.objects.all())
    random.seed(request.session.get('seed', random.randint(0,100)))
    random.shuffle(stores)
    context = {
      'stores': stores,
        'user': {
          'userid': request.session.get('id', None)
        }
    }
    request.session['start'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    return render(request, 'web/all.html', context)
  if request.method == "POST":
    print(datetime.now())
    print(datetime.strptime(request.session['start'],"%Y-%m-%d %H:%M:%S.%f"))
    duration = (datetime.now() - datetime.strptime(request.session['start'],"%Y-%m-%d %H:%M:%S.%f")).total_seconds()
    d = Decision(dec_store=Store.objects.get(pk=request.POST['decision']),dec_sub=Subject.objects.get(pk=request.session['id']),dec_duration=duration)
    d.save()
  return HttpResponseRedirect('survey')

@check_login
@log_visit
def details(request,store_id):
  # import json
  # with open("list.json",'r') as load_f:
  #   list_dict = json.load(load_f)
  context = {
    'user': {
      'setting': request.GET.get('setting') if request.GET.get('setting') else request.session.get('group'),
      'userid': request.session.get('id', None)
    },
    'store':{},
    'reviews': []
  }
  # for store in list_dict[:15]:
  #   if (str(store['store_id'].split('/')[-1]) == str(store_id)):
  #     context['store'] = store
  # for review in list_dict[16:]:
  #   if (str(review['store_id'].split('/')[-1]) == str(store_id)):
  #     context['reviews'].append(review)

  s = Store.objects.get(pk=store_id)
  context['store'] = s
  r = list(Review.objects.filter(review_store=s))
  random.seed(request.session.get('seed', random.randint(0,100)))
  random.shuffle(r)
  context['reviews'] = r
  return render(request, 'web/details.html', context)

@check_login
@log_visit
def survey(request):
  if request.method == "GET":
    s = Subject.objects.get(pk=request.session['id'])
    survey = Survey.objects.get(category=3,group=s.sub_group)
    qlist = Question.objects.filter(survey__id=survey.id).order_by('order')
    for q in qlist:
      q.options = Option.objects.filter(question=q.id).order_by('value')
    context = {
      'survey': survey,
      'qlist': qlist
      }
    return render(request, 'web/survey.html', context)

  if request.method == "POST":
    s = Subject.objects.get(pk=request.session['id'])
    survey = Survey.objects.get(category=3,group=s.sub_group)
    qlist = Question.objects.filter(survey__id=survey.id).order_by('order')
    for q in qlist:
      ans = request.POST[f"{q.id}"]
      ch = Choice(subject=Subject.objects.get(pk=request.session['id']),question=q,option=Option.objects.get(pk=ans))
      ch.save()
    return HttpResponseRedirect('goodbye')

@check_login
@log_visit
def goodbye(request):
  return render(request, 'web/goodbye.html')
  # else:
  #   context = {
  #     'questions': [
  #       '我曾经想过网络在线评论中存在虚假评论。',
  #       '在浏览餐厅评论时我注意到了警示信息并且认真阅读了它。',
  #       '我对我在该网站上选择的餐厅很满意。',
  #       '如果有第二次机会，我仍然会选择这家餐厅。',
  #       '我相信我所选择的餐厅在该网站上的同类同等餐厅中是最好的。',
  #       '在该网站上完成选择餐厅这一任务令人感觉很为难。',
  #       '在该网站上完成选择餐厅这一任务耗费了我很多精力。',
  #       '在该网站上完成选择餐厅这一任务太过复杂。',
  #       '我相信我选择的餐厅真实情况会与平台评论中描述的一致。',
  #       '我相信平台所提供的信息对我的消费决策有帮助。',
  #       '平台将所有的信息都坦诚地提供给用户，即使是有关产品或服务的负面信息。',
  #       '平台对用户的利益有所关心。',
  #       '在使用过程中，平台为用户承担了风险。',
  #       '我认为平台是站在用户这边的。'
  #     ]
  #   }

@csrf_exempt
@check_login
def log(request):
  logger(userid=request.POST.get('userid', None), action=request.POST.get('action', None), value=request.POST.get('value', None))
  return HttpResponse('a')



