from rest_framework import serializers
from app04.models import Game

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = "__all__"
        # exclude = ('user',)

        extra_kwargs = {
            "user":{'read_only':True}
        }