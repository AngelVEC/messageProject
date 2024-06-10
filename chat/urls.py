from chat.viewsets import ChatRoomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'testing', ChatRoomViewSet, basename = 'testing')
router.register(r'chatroom', ChatRoomViewSet, basename = 'chatroom')
urlpatterns = router.urls