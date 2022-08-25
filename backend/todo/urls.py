from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('tasks',views.TodoView,basename='task')



urlpatterns = router.urls