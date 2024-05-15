from rest_framework.serializers import ModelSerializer
from .models import Track, Playlist
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class TrackSerilizer(ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"
        

class PlaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"
        
        
class UserRegistration(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
        def validate(self, data):
            email = data.get('email')
            if User.objects.filter(email=email).exists():
                raise ValidationError({'error': 'User already exist with this email'})
            username= data.get('username')
            if User.objects.filter(username=username).exists():
                raise ValidationError({'error': 'username already exist'})
            
            return data
        
        def save(self):
            try:
                password = self.validated_data['password']      
                account = User(email = self.validated_data['email'],
                            username = self.validated_data['username'],)
                account.set_password(password)
                account.save()
                return account
            except Exception as e:
                return ValidationError(str(e))