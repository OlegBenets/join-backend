from rest_framework import serializers
from django.contrib.auth.models import User
        

class RegistrationsSerializer(serializers.ModelSerializer):
    repeated_passwort = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_passwort']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_passwort']
        email = self.validated_data['email']
        
        if pw != repeated_pw:
            raise serializers.ValidationError({'error': 'passwords dont match'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': 'email already exists'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(pw)
        account.save()
    
        return account