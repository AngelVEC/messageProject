from chat.models import ChatRoom, Message
from chat.serializers import ChatRoomSerializer,MessageSerializer
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from chat.serializers import userRegisterSerializer

class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class registerView(APIView) :
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        clean_data = request.data
        serializer = userRegisterSerializer(data=clean_data)

        return serializer.create(clean_data)