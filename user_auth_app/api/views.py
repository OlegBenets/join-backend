from rest_framework import generics
from .serializers import RegistrationsSerializer, CustomLoginSerializer
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from join_app.models import Contact
    
class RegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegistrationsSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            
            Contact.objects.create(
                user=saved_account, 
                name=saved_account.username, 
                email=saved_account.email,
                phone=None,  
                color="#00bee8"
            )
            
            token, created = Token.objects.get_or_create(user=saved_account)
            print(token.key)
            
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email
            }
            print(data)
        else:
            data=serializer.errors
            
        return Response(data)
    
class CustomLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = CustomLoginSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            
            data = {
                'token': token.key,
                'email': user.email, 
            }
            print(data)
        else:
            data=serializer.errors
        return Response(data)