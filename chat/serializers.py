from rest_framework import serializers, status
from chat.models import ChatRoom, Message
from django.contrib.auth.models import User
from rest_framework.response import Response


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

class userRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['all']

    def create(self, clean_data):
        if User.objects.filter(email=clean_data['email']).exists() or User.objects.filter(username=clean_data['username']).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        user_obj = User.objects.create_user(email=clean_data['email'], username = clean_data['username'], password= clean_data['password'])
        user_obj.save()
        return Response(status=status.HTTP_201_CREATED)