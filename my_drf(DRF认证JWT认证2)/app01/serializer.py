
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Group,Student

class GroupSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id','name')

class StudentSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ('id','name','age','group')