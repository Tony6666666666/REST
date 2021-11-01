from django.db import models

# Create your models here.
class User(models.Model):
    GENDERS = (
        (1,"男"),(2,"女")
    )
    name = models.CharField(max_length=10,verbose_name='名字')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    gender = models.IntegerField(choices=GENDERS,verbose_name='性别')
    pwd = models.CharField(max_length=64,verbose_name='密码')
