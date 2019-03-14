from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Store, Review, Subject, PreSurvey, Decision, PostSurvey


def index(request):
  # stores = Store.objects.all()
  # return HttpResponse(len(stores))
  context = {
    'questions': [
      {
        'q': '您的性别为：',
        'c': ['男','女']
      },
      {
        'q': '您的年龄段为：',
        'c': ['18岁以下','18-25岁','26-35岁','35岁以上']
      },
      {
        'q': '您最近三个月网络购物或使用点评网站（如大众点评）的平均频率为：',
        'c': ['每周一次或更多','每周一次或更多']
      },
      {
        'q': '您网络购物或使用点评网站时对评论的参考程度为：',
        'c': ['从不参考','','','','总是参考']
      },
    ]
  }
  return render(request, 'web/index.html',context)

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
  stores = Store.objects.all()
  return render(request, 'web/start.html', {'num':len(stores)})

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
  # survey = Survey.objects.get(id=1)
  # question_list = Question.objects.filter(survey__id=1)
  # for q in question_list:
  #   q.options = Option.objects.filter(question=q.id)
  # context = {
  #   'survey': survey,
  #   'question_list': question_list
  #   }
  if request.method == "POST":
    res = HttpResponseRedirect('register')
    res.delete_cookie('username')
    return res
  else:
    context = {
      'questions': [
        '我曾经想过网络在线评论中存在虚假评论。',
        '在浏览餐厅评论时我注意到了警示信息并且认真阅读了它。',
        '我对我在该网站上选择的餐厅很满意。',
        '如果有第二次机会，我仍然会选择这家餐厅。',
        '我相信我所选择的餐厅在该网站上的同类同等餐厅中是最好的。',
        '在该网站上完成选择餐厅这一任务令人感觉很为难。',
        '在该网站上完成选择餐厅这一任务耗费了我很多精力。',
        '在该网站上完成选择餐厅这一任务太过复杂。',
        '我相信我选择的餐厅真实情况会与平台评论中描述的一致。',
        '我相信平台所提供的信息对我的消费决策有帮助。',
        '平台将所有的信息都坦诚地提供给用户，即使是有关产品或服务的负面信息。',
        '平台对用户的利益有所关心。',
        '在使用过程中，平台为用户承担了风险。',
        '我认为平台是站在用户这边的。'
      ]
    }
    return render(request, 'web/survey.html', context)

def goodbye(request):
  return render(request, 'web/goodbye.html')


