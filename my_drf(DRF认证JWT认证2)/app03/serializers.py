import re
from rest_framework import serializers
from app03.models import User
from collections import OrderedDict

class ChoiceDisplayField(serializers.Field):
    def __init__(self,choices,**kwargs):
        self._choices = OrderedDict(choices)
        super(ChoiceDisplayField,self).__init__(**kwargs)

    #返回可读性良好的字符串而不是1, -1这样的数字
    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        for i in self._choices:
            if i == data or self._choices[i] == data:
                return i
        raise serializers.ValidationError("Acceptable values are {0}.".format(list(self._choices.values())))

class UserSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(max_length=11,min_length=11,required=True)

    pwd1 = serializers.CharField(max_length=64,write_only=True)

    # gender = serializers.CharField(source='get_gender_display')


    #支持可读可写
    GENDERS=(
        (1,"男"),(2,"女")
    )
    gender = ChoiceDisplayField(choices=GENDERS)

    class Meta:
        model = User
        fields = "__all__"

        #读的时候不必传，写的时候必传
        # extra_kwargs = {
        #     "pwd":{'write_only':True}
        # }

    # def to_representation(self, instance):
    #     representation = super(UserSerializer,self).to_representation(instance)
    #     representation['gender'] = instance.get_gender_display()
    #     return representation

    #validate和validate_phone  两个方法一定要有返回值，不然无效
    def validate_phone(self,phone):
        if not re.match(r'1[3456789]\d{9}',phone):
            raise serializers.ValidationError(r'手机号不符合规范')

        if User.objects.filter(phone=phone).all():
            raise serializers.ValidationError('手机号已被注册')

        return phone


    def validate(self, attrs):
        if attrs.get('pwd1') != attrs.get('pwd'):
            raise serializers.ValidationError('两次密码不一致')
        if 'pwd1' in attrs:
            attrs.pop('pwd1')  #验证后再删除
        return attrs