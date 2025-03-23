from django.urls import path, include
import user_auth_app.api.urls 
from rest_framework_nested import routers
from .views import ContactViewSet, TaskViewSet, SubTaskViewSet

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'contacts', ContactViewSet)
tasks_router = routers.NestedSimpleRouter(router, r'tasks', lookup='task')
tasks_router.register(r'sub_tasks', SubTaskViewSet, basename='task-subtasks')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(tasks_router.urls)),
    path("", include(user_auth_app.api.urls)),
]