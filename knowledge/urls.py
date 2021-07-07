from rest_framework.routers import SimpleRouter
from knowledge import views


router = SimpleRouter()

router.register(r'knowledge', views.KnoeledgeViewSet)

urlpatterns = router.urls
