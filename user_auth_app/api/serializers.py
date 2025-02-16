from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
        

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
    
    def validate_username(self, value):
        if not value.strip():
            raise serializers.ValidationError("Username darf nicht leer sein.")
        return value
    
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
    
    
class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("email and password are requirde.")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed("user with this email does not exist.")

        if not user.check_password(password):
            raise AuthenticationFailed("wront password.")

        return {'user': user}