from rest_framework.routers import DefaultRouter

from menu.views import MenuViewSet

router = DefaultRouter()
router.register(r"menu", MenuViewSet, basename="menu")

urlpatterns = router.urls
