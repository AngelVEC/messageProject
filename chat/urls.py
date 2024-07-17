from chat.viewsets import ChatRoomViewSet, MessageViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

from chat.views import sumNumbersView
from django.urls import path

router = DefaultRouter()
router.register(r'chatroom', ChatRoomViewSet, basename = 'chatroom')
router.register(r'message', MessageViewSet, basename = 'message')
router.register(r'users', UserViewSet)
urlpatterns = router.urls


urlpatterns += [
    path('sum_numbers/', sumNumbersView, name='sum_numbers'),
]