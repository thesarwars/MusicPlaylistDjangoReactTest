from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def Home(request):
    return HttpResponse("Hello Tahasin")

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if username and password:
            user = User.objects.filter(username=username).first()
            if user is not None and user.check_password(password):
                return Response({'error': False, 'message': 'User logged in successfully'}, status.HTTP_200_OK)
            return Response({'error': True, 'message': "username or password doesn't match"}, status.HTTP_404_NOT_FOUND)
        return Response({'error': True, 'message': 'username or password input missing'}, status.HTTP_400_BAD_REQUEST)