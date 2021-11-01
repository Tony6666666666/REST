from django.http import JsonResponse
from rest_framework import viewsets
# Create your views here.
from .models import *
from .serializer import StudentSerializer,GroupSerializer


def index(request):
    ctx = {
        'code':1,
        'msg':'ok',
        'data':{
            'user':[
                {
                    'name':'老王',
                    'age': 12,
                },
                {
                    'name': '老李',
                    'age': 18,
                },
                {
                    'name': '老赵',
                    'age': 19,
                }
            ]
        }
    }
    return JsonResponse(ctx)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class GroupViewSet(viewsets.ModelViewSet):
    #要序列化的数据
    queryset = Group.objects.all()
    #要是哪个序列化类
    serializer_class = GroupSerializer
