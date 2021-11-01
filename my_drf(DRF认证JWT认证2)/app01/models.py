from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=5,verbose_name='小组名称')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=10,verbose_name='学生名称')
    age = models.IntegerField(verbose_name='学生年龄')
    group = models.ForeignKey(to=Group,on_delete=models.CASCADE)


