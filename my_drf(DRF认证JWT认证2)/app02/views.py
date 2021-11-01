from django.http import HttpResponse
from .models import *
# Create your views here.
from .serializers import ArticleSerializer2, CategorySerializer, TagSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


#封装得到的HttpResponse
class JSONResponse(HttpResponse):
    def __str__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__str__(content,**kwargs)


#获取多条数据（所有对象）
@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        arts = Article.objects.all()
        ser = ArticleSerializer2(instance=arts,many=True,context = {'request': request})
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data,content_type='application/json',status=200)

    elif request.method == 'POST':
        #把前端传过来的json数据转换成python对象的数据类型
        data = JSONParser().parse(request)

        ser = ArticleSerializer2(data=data,context = {'request': request})
        if ser.is_valid():
            ser.save()
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data, content_type='application/json', status=201)
        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)


# 获取单条数据（单个对象）
@csrf_exempt
def article_detail(request,pk):
    try:
        art = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        ser = ArticleSerializer2(instance=art,context = {'request': request})
        return JSONResponse(ser.data,status=200)

        #JSONResponse和HttpResponse的区别在于JSONResponse自带content_type，故不用写

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        ser = ArticleSerializer2(instance=art,data=data,context = {'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data,status=201)
        return JSONResponse(ser.errors,status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        ser = ArticleSerializer2(instance=art,data=data,partial=True,context = {'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data,status=201)
        return JSONResponse(ser.errors,status=400)

    elif request.method == 'DELETE':
        art.delete()
        return HttpResponse(status=204)

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        arts = Category.objects.all()
        ser = CategorySerializer(instance=arts,many=True,context = {'request': request})
        return JSONResponse(ser.data,content_type='application/json',status=200)

    elif request.method == 'POST':
        #把前端传过来的json数据转换成python对象的数据类型
        data = JSONParser().parse(request)
        ser = CategorySerializer(data=data,context = {'request': request})

        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data, content_type='application/json', status=201)
        return JSONResponse(ser.errors, content_type='application/json', status=400)

@csrf_exempt
def category_detail(request,pk):
    try:
        art = Article.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        ser = CategorySerializer(instance=art,context = {'request': request})
        return JSONResponse(ser.data,status=200)
        #JSONResponse和HttpResponse的区别在于JSONResponse自带content_type，故不用写

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        ser = CategorySerializer(instance=art,data=data,context = {'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data,status=201)
        return JSONResponse(ser.errors,status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        ser = CategorySerializer(instance=art,data=data,partial=True,context = {'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data,status=201)
        return JSONResponse(ser.errors,status=400)

    elif request.method == 'DELETE':
        art.delete()
        return HttpResponse(status=204)


@csrf_exempt
def tag_list(request):
    if request.method == 'GET':
        tag = Tag.objects.all()
        ser = TagSerializer(instance=tag,many=True,context = {'request': request})
        return JSONResponse(ser.data,content_type='application/json',status=200)

    elif request.method == 'POST':
        #把前端传过来的json数据转换成python对象的数据类型
        data = JSONParser().parse(request)
        ser = TagSerializer(data=data,context = {'request': request})

        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data, content_type='application/json', status=201)
        return JSONResponse(ser.errors, content_type='application/json', status=400)

@csrf_exempt
def tag_detail(request,pk):
    try:
        tag = Tag.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        ser = TagSerializer(instance=tag,context = {'request': request})
        return JSONResponse(ser.data,status=200)
        #JSONResponse和HttpResponse的区别在于JSONResponse自带content_type，故不用写

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        ser = TagSerializer(instance=tag,data=data,context = {'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data,status=201)
        return JSONResponse(ser.errors,status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        ser = TagSerializer(instance=tag,data=data,partial=True,context = {'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data,status=201)
        return JSONResponse(ser.errors,status=400)

    elif request.method == 'DELETE':
        tag.delete()
        return HttpResponse(status=204)

