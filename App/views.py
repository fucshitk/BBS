import hashlib
import json
import os
import io
import random
import string

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import *
from Bank.settings import BASE_DIR, MEDIA_ROOT,STATIC_URL



#首页
def home(request):
    return render(request,'home.html')
#主页
def index(request):
    return base(request, typeid=1, A_type='shici.html')

#注册页
def register(request):
    '''
    注册
    :param request:
    :return:
    '''
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        uname = request.POST.get('uname',None)
        upwd = request.POST.get('upwd', None)
        upwd2 = request.POST.get('upwd2', None)

        vcode = request.POST.get('vcode',None)

        user = User.objects.filter(uname=uname).first()

        if not user:
            # uiconFile = request.FILES.get('uicon',None)

            #手动存储上传的文件

            # fp = os.path.join(MEDIA_ROOT,'new-'+uiconFile.name)
            # with open(fp,'wb') as f:
            #     for buffer in uiconFile.chunks():
            #         f.write(buffer)

            # 校验验证码
            sessvcode = request.session.get('vcode',None)
            #print(">>>>>>>>>>>>>>>>>>>",sessvcode,type(sessvcode))
            if vcode and sessvcode and vcode.lower()==sessvcode.lower():
                if uname and upwd and upwd2 and upwd == upwd2:
                    #保存注册信息
                    u = User()
                    u.uname = uname
                    u.upwd = upwd
                    u.save()

                    return redirect(reverse("app:shici"))
                else:
                    return HttpResponse('两次密码不一致')

            else:
                return HttpResponse('验证码错误')
        else:
            return HttpResponse('用户名已存在')


#登录页
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        uname = request.POST.get('uname',None)
        upwd = request.POST.get('upwd',None)
        vcode = request.POST.get('vcode',None)
        sessvcode = request.session.get('vcode',None)
        print(uname,upwd,vcode, sessvcode,generate_password(upwd))
        # 验证
        if not vcode and not uname and not upwd:
            return render(request, 'login.html')
        elif not vcode:
            return HttpResponse('<script>alert("验证码不能为空");window.history.back()</script>')
        elif vcode.lower()!=sessvcode.lower():
            return HttpResponse('<script>alert("验证码错误");window.history.back()</script>')
        else:
            print(vcode,sessvcode)
            user = User.objects.filter(uname=uname).first()
            if user:
                if uname and upwd:
                    if user.upwd == upwd and user:
                        print('密码验证',user.upwd,upwd)
                        request.session['uname'] = user.uname
                        request.session['uicon'] = user.uicon.name
                        request.session['userid'] = user.id
                        print(uname, user.upwd, vcode, sessvcode, upwd)
                        return redirect(reverse("app:shici"))
                    else:
                        return HttpResponse('<script>alert("用户名或密码错误");window.history.back()</script>')
                else:
                    return HttpResponse('<script>alert("用户名和密码不能为空");window.history.back()</script>')
            else:
                return HttpResponse('<script>alert("该用户名不存在");window.history.back()</script>')


#登出
def logout(request):
    resp = redirect(reverse('app:login'))

    #将utoken从前端拿走
    resp.delete_cookie('utoken')

    #清除session
    request.session.flush()
    return resp
#个人中心页
def mine(request):
    uname = request.session.get('uname',None)
    if uname:
        user = User.objects.get(uname=uname)
        bgimg = user.bgimg
        uicon = user.uicon
        data={
            'uname':uname,
            'uicon':'http://127.0.0.1:8000/uploads/'+str(uicon),
            'bgimg':'http://127.0.0.1:8000/uploads/'+str(bgimg),
            'user':user,
        }
        return render(request,'mine.html',context=data)
    else:
        return register(reverse('app:login'))


#验证码
def getvcode(request):
    '''绘制验证码,并返回验证码'''
    #随机生成验证码里的字
    population = string.ascii_letters+string.digits
    letterlist = random.sample(population,4)
    vcode = ''.join(letterlist)

    # 保存验证码到session，才能校验
    request.session['vcode']=vcode
    # print(vcode)
    #需要一个画布
    image = Image.new('RGB',(100,33),color=(255,255,255))
    # image = Image.new('RGB',(100,33),color=getRandomColor())
    #画笔
    draw = ImageDraw.Draw(image)
    #导入字体
    path = os.path.join(BASE_DIR,'static','fonts', 'cambriab.ttf')
    #用字体
    font = ImageFont.truetype(font=path,size=20)
    # 绘制文字
    for i in range(len(vcode)):
        # draw.text((12+20*i,3),vcode[i],fill=getRandomColor(),font=font)
        draw.text((12+20*i,3),vcode[i],fill=(0,0,0),font=font)

    #添加噪点--一百个
    for j in range(200):
        population = (random.randint(0,80),random.randint(0,25))
        # draw.point(population,fill=getRandomColor())
        draw.point(population,fill=(255,255,255))

    #返回验证码字节数据
    #创建字节容器用来存放验证码图片
    buffer = io.BytesIO()
    #将验证码内容丢到buffer
    image.save(buffer,'png')
    return HttpResponse(buffer.getvalue(),'image/png')

#绘制验证码
def getRandomColor():
    '''随机颜色'''
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    return (red,green,blue)

def base(request,typeid=2,A_type='sanwen.html'):
    uname = request.session.get('uname',None)
    if uname:
        user = User.objects.get(uname=uname)
        arts = Article.objects.filter(A_type_id=typeid).order_by('-add_time')
        print(arts)
        if arts:
            arts = Article.objects.filter(A_type_id=typeid)
            data = {
                'uname': uname,
                'uicon':  'http://127.0.0.1:8000/uploads/'+str(user.uicon),
                'arts': arts,
            }
            return render(request,A_type,context=data)
        else:

            data = {
                'uname': uname,
                'uicon':  'http://127.0.0.1:8000/uploads/'+str(user.uicon),
                'arts': arts,
            }
            return render(request,A_type,context=data)
    else:
        return redirect(reverse('app:login'))

#诗词页
def shici(request):
    return base(request, typeid=1, A_type='shici.html')

#散文页
def sanwen(request):
    return base(request, typeid=2, A_type='sanwen.html')

#小说
def xiaoshuo(request):
    return base(request,typeid=3,A_type='xiaoshuo.html')

#寓言
def yuyan(request):
    return base(request, typeid=4, A_type='yuyan.html')

#童话
def tonghua(request):
    return base(request, typeid=5, A_type='tonghua.html')

#日志
def rizhi(request):
    return base(request, typeid=6, A_type='rizhi.html')

#段子
def duanzi(request):
    return base(request, typeid=7, A_type='duanzi.html')

#吹水
def chuishui(request):
    return base(request, typeid=8, A_type='chuishui.html')

#发表文章页
def addact(request):
    if request.method == 'GET':
        return render(request,'addact.html')
    else:
        uname = request.session.get('uname',None)
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)
        a_type = request.POST.get('A_type',None)
    if title and content and a_type:
        uid = User.objects.get(uname=uname).id
        art = Article()
        art.title = title
        art.content = content
        art.A_type_id = a_type
        art.author_id = uid
        art.save()
        return HttpResponse('<script>alert("发表成功")</script>')
    elif not title:
        return HttpResponse('<script>alert("标题不能为空");window.history.back()</script>')
    elif not content:
        return HttpResponse('<script>alert("正文不能为空");window.history.back()</script>')
    elif not a_type:
        return HttpResponse('<script>alert("没有选类型");window.history.back()</script>')


#文章详情页
def readart(request,artid):
    art = Article.objects.filter(id=artid).first()
    if art:
        uname = request.session.get('uname', None)
        user = User.objects.get(uname=uname)
        uicon = request.session.get('uicon', None)
        pinglun = request.POST.get('pinglun', None)
        print(pinglun)
        if pinglun:
            c = Comment()
            c.pinglun = pinglun
            c.belong_user_id = user.id
            c.belong_art_id = artid
            c.save()

        com = Comment.objects.filter(belong_art_id=artid)
        data = {
            'uname': uname,
            'uicon': 'http://127.0.0.1:8000/uploads/' + uicon,
            'art':art,
            'com':com,
        }
        print(com)
        return render(request,'readart.html',context=data)
    else:
        return HttpResponse('<script>alert("文章可能删除了.....");window.history.back()</script>')


#设置页
def set(request):
    uname = request.session.get('uname', None)
    if request.method == 'GET':
        if uname:
            user = User.objects.get(uname=uname)
            uicon = user.uicon
            data={
                'uname':uname,
                'uicon':'http://127.0.0.1:8000/uploads/'+str(uicon),
                'bgimg': 'http://127.0.0.1:8000/uploads/' + str(user.bgimg),
                'user':user,
            }
            return render(request, 'set.html', context=data)


    else:
        uicon = request.FILES.get('uicon','uicon/default.jpg')
        bgimg = request.FILES.get('bgimg','bgimg/welcome.gif')
        gender = request.POST.get('gender',None)
        signature = request.POST.get('signature',None)
        mobile = request.POST.get('mobile',None)
        email = request.POST.get('email',None)
        print(uicon,gender,bgimg)
        user = User.objects.get(uname=uname)
        # if uicon or gender or bgimg or signature or mobile or email:
        user.uname = uname
        user.uicon = uicon
        user.gender = gender
        user.signature = signature
        user.mobile = mobile
        user.email = email
        user.bgimg = bgimg
        user.save()
        data = {
            'uname': uname,
            'uicon': 'http://127.0.0.1:8000/uploads/'+str(user.uicon),
            'bgimg': 'http://127.0.0.1:8000/uploads/'+str(user.bgimg),
            'user': user,
        }
        print(data['bgimg'],data['uicon'])
        return render(request, 'set.html', context=data)
        # else:
        #     data = {
        #         'uname': uname,
        #         'uicon': 'http://127.0.0.1:8000/uploads/' + str(user.uicon),
        #         'bgimg': 'http://127.0.0.1:8000/uploads/' + str(user.bgimg),
        #         'user': user,
        #     }
        #     # return HttpResponse("<script>alert('未做更改，无须保存')window.history.back()</script>")
        #     return render(request, 'set.html', context=data)

# TODO 生成密码
def generate_password(password):

    sha = hashlib.sha512()

    sha.update(password.encode("utf-8"))

    return sha.hexdigest()


# 校验用户名是否可用
def check_user(request):
    username = request.GET.get("username")
    users = User.objects.filter(username=username)

    data = {
        "msg":"ok",
        "status":"200",
    }

    if users.exists():
        data["desc"] = "用户已存在"
        data["msg"] = "fail"
        data["status"] = "900"
    else:
        data["desc"] = "用户名可用"
    return JsonResponse(data)

#ta人资料页
def ta(request,uid):
    uname = request.session.get('uname',None)
    uicon = request.session.get('uicon',None)
    if uname:
        user = User.objects.get(id=uid)
        data={
            'uname':uname,
            'uicon':'http://127.0.0.1:8000/uploads/'+uicon,
            'bgimg': 'http://127.0.0.1:8000/uploads/' + str(user.bgimg),
            'user':user,
        }
        return render(request,'ta.html',context=data)
    else:
        return register(reverse('app:login'))


def getIP(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']
#
# #收藏功能
# def like(request):
#     data = {
#         'status': 900,
#         'msg': 'add failed!'
#     }
#
#     # 哪个用户，对哪篇文章收藏
#     userid = request.session.get('userid', None)
#     if userid:
#         artid = request.GET.get('artid', None)
#         likes = Likes.objects.get(art_id=artid)
#         like_num = likes.like_num + 1
#         likes.save()
#
#         data['status'] = 200
#         data['msg'] = 'add ok!'
#         data['like_num'] = likes.like_num
#
#     else:
#         data['status'] = 901
#         data['msg'] = 'not login'
#
#     return JsonResponse(data)


#错误页面定制

# 错误页面
def page_not_found(request):
    return render(request, 'mstp_404/index.html')


def page_error(request):
    return render(request, '500.html')


def permission_denied(request):
    return render(request, 'out/403.html')

#搜索功能
def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        print('请输入关键词')
        return render(request, 'SearchResult.html', {'error_msg': error_msg})

    else:
        post_list = Article.objects.filter(title__icontains=q)
        print(post_list)
        return render(request, 'SearchResult.html', {'error_msg': error_msg,
                                                   'post_list': post_list})


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def terminal_svr(request):
  # 这里利用了django自身的登陆验证系统
  if not request.user.is_authenticated():
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))

  a = {}
  a["result"] = "post_success"
  return HttpResponse(json.dumps(a), content_type='application/json')

#关于
def about(request):
    if request.method == 'GET':
        return render(request,'about.html')
    else:
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
        massage = request.POST.get('massage',None)
        if name and email and massage:
            m = Message()
            m.name = name
            m.email = email
            m.massage = massage
            m.save()
            return HttpResponse('<script>alert("留言成功")</script>')
        else:
            return render(request,'about.html')