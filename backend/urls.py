from rest_framework.routers import SimpleRouter
from backend import views


router = SimpleRouter()

router.register(r'course', views.CourseViewSet)
router.register(r'vocabulary', views.VocabularyViewSet)
router.register(r'accent', views.AccentViewSet)
router.register(r'senses', views.SensesViewSet)
router.register(r'exercise', views.ExerciseViewSet)


urlpatterns = router.urls
