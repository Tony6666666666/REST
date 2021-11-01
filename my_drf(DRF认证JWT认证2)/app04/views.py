import permission as permission
from rest_framework import generics, permissions
from .serializers import GameSerializer
from .models import Game
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from .permissions import IsOwnOrReadOnly

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnOrReadOnly]


