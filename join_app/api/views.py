from rest_framework import viewsets
from .serializers import ContactSerializer, TaskSerializer
from join_app.models import Contact, Task
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStaffOrReadOnly, IsAdminForDeleteOrPatchAndReadOnly, IsOwnerOrAdmin

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    #permission_classes = [IsAuthenticated]
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = [IsAuthenticated]
