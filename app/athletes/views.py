from rest_framework.generics import RetrieveAPIView
from .models import BasketballPlayer, SoccerPlayer
from .serializers import BasketballPlayerSerializer, SoccerPlayerSerializer


class BasketballPlayerView(RetrieveAPIView):
    queryset = BasketballPlayer.objects.all()
    serializer_class = BasketballPlayerSerializer
    lookup_field = "slug"


class SoccerPlayerView(RetrieveAPIView):
    queryset = SoccerPlayer.objects.all()
    serializer_class = SoccerPlayerSerializer
    lookup_field = "slug"
