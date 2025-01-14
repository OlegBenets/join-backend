from django.urls import path, include
import user_auth_app.api.urls 
from rest_framework import routers
from .views import ContactViewSet, TaskViewSet

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(user_auth_app.api.urls)),
]
