from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='分类',max_length=10)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(verbose_name='标签名字',max_length=10)
    create_time = models.DateTimeField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(verbose_name='标题',max_length=100)
    vnum = models.IntegerField(verbose_name='浏览量')
    content = models.TextField(verbose_name='内容')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='articles')
    tags = models.ManyToManyField(Tag,related_name='artlcles')

    def __str__(self):
        return 'Article:%s'%self.title

    class Meta:
         verbose_name = u'文章'
         verbose_name_plural = verbose_name


