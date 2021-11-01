from django.utils.timezone import now
from rest_framework import serializers
from .models import *

#普通序列化
# class ArticleSerializer1(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100,required=True)
#     vnum = serializers.IntegerField(required=True)
#     content = serializers.CharField()
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.vnum = validated_data.get('vnum',instance.vnum)
#         instance.content = validated_data.get('content',instance.content)
#
#         instance.save()
#         return instance

# 模型序列化1
# class ArticleSerializer2(serializers.ModelSerializer):
#     # categorys = serializers.StringRelatedField()     #StringRelatedField字段
#
#     class Meta:
#         model = Article
#         # fields = ('id','title','categorys')
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     # articles = serializers.StringRelatedField(many=True)  #StringRelatedField字段
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#         # fields = ('id', 'name', 'articles')


#模型序列化2
# class ArticleSerializer2(serializers.ModelSerializer):
#     # categorys = serializers.StringRelatedField()     #StringRelatedField字段

#     categorys = serializers.HyperlinkedIdentityField(  #HyperlinkedIdentityField字段
#         view_name='app02:category-detail',
#         # read_only=True,
#     )
#
#     class Meta:
#         model = Article
#         # fields = ('id','title','categorys')
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     # articles = serializers.StringRelatedField(many=True)  #StringRelatedField字段

#     articles = serializers.HyperlinkedIdentityField(        #HyperlinkedIdentityField字段
#         view_name='app02:article-detail',
#         many=True,
#         # read_only=True,
#     )
#     class Meta:
#         model = Category
#         # fields = '__all__'
#         fields = ('id', 'name', 'articles')


#模型序列化3
# HyperlinkedModelSerializer
# class ArticleSerializer2(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Article
#         # fields = ('id','title','categorys')
#         fields = '__all__'
#
#         extra_kwargs = {
#             'url': {'view_name': 'app02:article-detail', 'lookup_field': 'pk'},
#             'category': {'view_name': 'app02:category-detail', 'lookup_field': 'pk'},
#         }
#
# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         # fields = '__all__'
#         fields = ('id', 'name', 'articles','url')
#
#         extra_kwargs = {
#             'url':{'view_name':'app02:category-detail','lookup_field':'pk'},
#             'articles':{'view_name':'app02:article-detail','lookup_field':'pk'},
#         }


#序列化嵌套4
#ModelSerializer
# class ArticleSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         # fields = ('id','title','categorys')
#         fields = '__all__'
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = ArticleSerializer2(many=True)
#     class Meta:
#         model = Category
#         # fields = '__all__'
#         fields = ('id', 'name', 'articles','url')


#深度5
#depth
# class ArticleSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         # fields = ('id','title','categorys')
#         fields = '__all__'
#         depth = 2
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = ArticleSerializer2(many=True)
#     class Meta:
#         model = Category
#         # fields = '__all__'
#         fields = ('id', 'name', 'articles')

#序列化方法6
#SerializerMethodField
# class ArticleSerializer2(serializers.ModelSerializer):
#     # categorys = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Article
#         # fields = ('id','title','categorys')
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#
#
#     count = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Category
#         # fields = '__all__'
#         fields = ('id', 'name', 'articles','count')
#
#     def get_count(self,obj):
#         return obj.articles.count()

#source
# class ArticleSerializer2(serializers.ModelSerializer):
#     category = serializers.IntegerField(source='category.id')
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     article = serializers.CharField(source='articles.all')
#     # article = serializers.CharField(source='article_set.all')  #如果没有related_name
#     class Meta:
#         model = Category
#         fields = ('id', 'name','article')

class ArticleSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        # depth = 2      #打开depth后只支持序列化而不支持反序列化

    #决定每一个字段的返回值
    def to_representation(self, instance):
        representation = super(ArticleSerializer2,self).to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        representation['tags'] = TagSerializer(instance.tags,many=True).data
        return representation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class TagSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = Tag
        fields = "__all__"


