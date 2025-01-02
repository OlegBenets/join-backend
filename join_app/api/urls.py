from django.urls import path, include

from .views import ContactList, TaskList


urlpatterns = [
    path('contacts', ContactList.as_view()),
    path('tasks', TaskList.as_view()),
]
