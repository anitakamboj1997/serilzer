from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# class SignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password','first_name','last_name']
#     def validate_email(self, email):
#             print(email)
#             email = User.objects.get(email = email)
#             if email:
#                 raise serializers.ValidationError("alredy exist")
#             else:
#                 return email
       
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)
# class SignupSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128)
#     email = serializers.EmailField()
#     first_name =  serializers.CharField(max_length=255)
#     last_name =  serializers.CharField(max_length=255)
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.save()
#         return instance
#     def validate_username(self, username):
#             print(username)
#             email = User.objects.get(username = username)
#             if username:
#                 raise serializers.ValidationError("alredy exist")
#             else:
#                 return email    
class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Event
        fields = '__all__'


class MainSerializer(serializers.ModelSerializer): 
    event = EventSerializer()

    class Meta: 
        model = Main
        fields = '__all__'

    def create(self, validated_data):
        event_data = validated_data.pop('event')
        event = Event.objects.get(id=event_data['id'])
        main = Main.objects.create(event=event, **validated_data)
        return main

    def update(self,instance, validated_data):
        print(instance,"instance")
        event_data = validated_data.pop('event')
        print(event_data)
        instance.event_data = validated_data.pop('event')
        instance.event = Event.objects.get(id=event_data['id'])
        instance.save()
      
        return instance


