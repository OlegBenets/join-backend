from rest_framework import viewsets
from .serializers import ContactSerializer, TaskSerializer, SubTaskSerializer
from join_app.models import Contact, Task, SubTask
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStaffOrReadOnly, IsAdminForDeleteOrPatchAndReadOnly, IsOwnerOrAdmin

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    
    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return SubTask.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs['task_pk']  
        task = Task.objects.get(pk=task_id)  
        serializer.save(task=task)