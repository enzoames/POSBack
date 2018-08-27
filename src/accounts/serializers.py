from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import *
from django.contrib.postgres.fields import JSONField
import json


# This Serializer is invoked for requests on rest-auth/user. It returns basic information about user
class UserSerializer(serializers.ModelSerializer):
	request_login = serializers.SerializerMethodField()
	request_load = serializers.SerializerMethodField()
	
	def get_request_login(self, obj):
		returned_value = False
		try:
			if self.context['request'].method == 'POST':
				returned_value =  True
			else:
				returned_value = False
		except:
			returned_value = False

		return returned_value

	def get_request_load(self, obj):
		returned_value = False
		try:
			if self.context['request'].method == 'POST':
				returned_value =  False
			else:
				returned_value = True
		except:
			returned_value = False

		return returned_value
		
	class Meta:
		model = User
		exclude = ('password', 'groups', 'joined', 'user_permissions', 'updated_at', 'created_at')


class SportaRegistrationSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('email', 'credential', 'first_name', 'last_name')

	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			if value is not None:
				setattr(instance, key, value)		
		instance.save()

		return instance


class UserBasicInfoSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

	def update(self, instance, validated_data):
		for key in validated_data:
			if validated_data[key] is not None:
				setattr(instance, key, validated_data[key])

		instance.save()


class BaseUserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'username', 'first_name', 'last_name')
