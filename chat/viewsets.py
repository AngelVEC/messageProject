from chat.models import ChatRoom
from chat.serializers import ChatRoomSerializer
from rest_framework import viewsets


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer