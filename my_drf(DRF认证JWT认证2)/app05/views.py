from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework.authentication import BasicAuthentication,TokenAuthentication,SessionAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
import time,hashlib
from rest_framework import exceptions
from .permissions import MyPermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .throttlings import VisitThrottling

def get_md5(user):
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        ret = {'code':1,'msg':None,'data':{}}
        user = request._request.POST.get('username')
        pwd = request._request.POST.get('password')
        obj = User.objects.filter(username=user,password=pwd).first()
        if not obj:
            ret['code'] = -1
            ret['msg'] = '用户名或密码错误'
        token = get_md5(user)
        UserToken.objects.update_or_create(user=obj,defaults={'token':token})
        ret['token'] = token
        return JsonResponse(ret)

class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        obj = UserToken.objects.filter(token=token).first()
        if not obj:
            raise exceptions.AuthenticationFailed('验证失败')
        else:
            return (obj.user,obj)



class CartView(APIView):
    #以下的都是局部的认证，若需要全局认证，则需要在settings里面写

    #基于哪个账号登录认证的
    # authentication_classes = [BasicAuthentication,TokenAuthentication,SessionAuthentication]

    #基于自己写的验证类
    # authentication_classes = [MyAuthentication]

    #基于jwt验证
    authentication_classes = [JSONWebTokenAuthentication]


    # 只有登录才能访问
    # permission_classes = [IsAuthenticated]

    #自己写的权限认证
    # permission_classes = [MyPermission]

    #局部节流
    throttle_classes = [VisitThrottling]  #不需认证
    def get(self,request,*args,**kwargs):
        ctx = {
            "code":1,
            "msg":"ok",
            "data":{
                "goods":[
                    {
                        "name": "苹果",
                        "price":12
                    },
                    {
                        "name": "香蕉",
                        "price": 13
                    },
                ]
            }
        }
        return JsonResponse(ctx)

    def put(self,request,*args,**kwargs):
        return HttpResponse('ok')
