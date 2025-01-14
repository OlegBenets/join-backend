from django.urls import path
from .views import RegistrationView, CustomLoginView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='singup'),
    path('login/', CustomLoginView.as_view(), name='login')
]