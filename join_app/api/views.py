from rest_framework import generics

from .serializers import ContactSerializer, TaskSerializer

from join_app.models import Contact, Task

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
        