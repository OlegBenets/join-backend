from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ContactSerializer, TaskSerializer

from join_app.models import Contact, Task

@api_view(['GET', 'POST'])
def contacts_view(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True,)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
@api_view()
def contacts_detail_view(request, pk):
    if request.method == 'GET':
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
        
      
@api_view(['GET', 'POST'])
def tasks_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True,)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
@api_view()
def tasks_detail_view(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)