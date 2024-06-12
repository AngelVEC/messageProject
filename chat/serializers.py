from rest_framework import serializers
from chat.models import ChatRoom, Message

# for API
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id','name']
        #if want to show all use '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'