from django.shortcuts import render, HttpResponse
import random
import datetime

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def dinner(request):
    box = ['치킨','메뚜기','개구리','롯데리아']
    dinner = random.choice(box)
    # render 필수인자
    # 1) request, 2) template 파일(html)
    # render 선택인자
    # 3) dictionary : 템플릿에서 쓸 변수 값을 정의

    return render(request, 'home/dinner.html', {'dinner':dinner,'box':box})
    # zai flask return ('dinner.html',~~)
    # template은 기본적으로 문법이 jinja2랑 같은데, 장고에서는 DTL을 쓴다.
    # Django template Language

def cube(request, num):
    return render(request, 'home/cube.html',{'num':num,'res':num**3})

def ping(request):
    return render(request, 'home/ping.html')

def pong(request):
    msg = request.GET.get('message')
    return render(request, 'home/pong.html',{'msg':msg})

def user_new(request):
    return render(request, 'home/user_new.html')
    
def user_read(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return render(request, 'home/user_read.html',{'username':username,'password':password})
    
def template_example(request):
    my_dict = {'name':'kim','nickname':'edutak','age':100}
    my_list = ['자장면','짬뽕','탕수육','양장피']
    my_sentence = 'Life is short, you need python!'
    messages = ['apple','banana','cucumber','mango']
    datetimenow = datetime.datetime.now()
    empty_list = []
    return render(request, 'home/template_example.html',{'my_dict':my_dict,'my_list':my_list,
    'my_sentence':my_sentence,'messages':messages,'empty_list':empty_list,'datetimenow':datetimenow})
    
def static_example(request):
    return render(request, 'home/static_example.html')