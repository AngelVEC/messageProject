from rest_framework import serializers
from chat.models import ChatRoom

# for API
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id','name']
        #if want to show all use '__all__'