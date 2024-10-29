from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status 
from django.contrib.auth import authenticate, login
from .serializers import UserSerializers

# class RegisterView(APIView):
@api_view(['POST'])
def RegisterView(request):
    serializer = UserSerializer(data =request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Resposne(serializer.errors,status=status.HTTP_404_NOT_FOUND)


# class LoginView(APIView):
@api_view(['POST'])
def LoginView(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return Response({"Login Successfully"})
    
    return Response({"Invalid"})
        # User is authenticated
        
        


# Create your views here.

