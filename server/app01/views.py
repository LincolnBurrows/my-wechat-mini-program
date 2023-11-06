from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
from server.settings import TENCENT_KEY
from app01.models import User


def index(request):
    is_login = request.session.get('is_login', None)
    print(f'is_login: {is_login}')
    if is_login:
        return redirect('/info/')
    return render(request, 'index.html')


# 账户注册
def reg(request):
    username = request.POST.get('username', None)
    pwd = request.POST.get('pwd', None)

    print(f'{username} - {pwd}')

    if username and pwd:
        # User.objects.create(username=username, pwd=pwd)
        new_user = User(username=username, pwd=pwd)
        new_user.save()
        return redirect('/index/')
    else:
        return HttpResponse('注册错误')


# 账户登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)  # POST要大写
        pwd = request.POST.get('pwd', None)
        print(f'{username} -  {pwd}')

        if username and pwd:
            res = User.objects.filter(username=username, pwd=pwd).first()
            # user_list = list(User.objects.all().values())
            # user_list = User.get_all()
            # print(user_list)
            print(res)
            if res:
                request.session['is_login'] = True
                # request.session.set_expiry(7 * 24 * 3600)  # 设置session过期时间为一周后
                return redirect('/info/')
            else:
                return HttpResponse('登录错误')
        else:
            return HttpResponse('登录错误')
    else:
        return HttpResponse('登录错误')


# 所有账户信息
def info(request):
    is_login = request.session.get('is_login', None)
    if is_login:
        print(TENCENT_KEY)
        user_list = list(User.objects.all().values())
        print(user_list)
        return render(request, 'info.html', {'user_list': user_list})
    return redirect('/index/')

# 注销登录
def signout(request):
    print('signout')
    request.session.flush()
    # del request.session['is_login']
    #request.session.clear()
    return JsonResponse({'msg':'success'})

# CBV TEST
from django.views import View


class test(View):
    def get(self, request, *args, **kwargs):
        # 在这里编写您的自定义逻辑
        request.session['user'] = 'u1'
        return HttpResponse(f"user:u1, session_id:{request.session.session_key}")

    def post(self, request, *args, **kwargs):
        # 在这里编写您的自定义逻辑
        return HttpResponse("post 这是自定义视图的结果")
