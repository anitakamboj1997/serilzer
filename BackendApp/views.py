from datetime import date

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework.authentication import TokenAuthentication

from .serializers import *
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER =  api_settings.JWT_ENCODE_HANDLER


# class Signup(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = SignupSerializer
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Signup(APIView):
    permission_classes = (AllowAny,)
    serializer_class = MainSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Update(APIView):
    permission_classes = (AllowAny,)
    serializer_class = MainSerializer  


    def get_obj(self, id):
        try:
            obj = Main.objects.get(id=id)
            return obj
        except:
            return False    


    def put(self, request, id):
        obj = self.get_obj(id)
        if obj:
            serializer = self.serializer_class(obj, data=request.data)
       
            if serializer.is_valid():
                try:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except:
                    return Response(serializer.errors, status=status.HTTP_201_CREATED)
          
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Login(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)
            if user:
                    token,created = Token.objects.get_or_create(user=user)
                    print(type(token))
                    return Response({'token': token.key},
                                        status=status.HTTP_200_OK)
            else:
                content = {'detail':
                           _('Unable to login with provided credentials.')}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
                       
class Logout(APIView):
    
    authentication_classes = [TokenAuthentication]
    def get(self, request, format=None):
        """
        Remove all auth tokens owned by request.user.
        """
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        content = {'success': _('User logged out.')}
        return Response(content, status=status.HTTP_200_OK)


