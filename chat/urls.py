from chat.viewsets import ChatRoomViewSet,MessageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'chatroom', ChatRoomViewSet, basename = 'chatroom')
router.register(r'message', MessageViewSet, basename = 'message')
urlpatterns = router.urls