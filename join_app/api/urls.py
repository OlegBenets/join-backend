from django.urls import path, include

from .views import contacts_view, tasks_view, contacts_detail_view, tasks_detail_view


urlpatterns = [
    path('contact/', contacts_view),
    path('contact/<int:pk>/', contacts_detail_view),
    path('task/', tasks_view),
    path('task/<int:pk>/', tasks_detail_view),
]
