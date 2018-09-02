from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import detail_route, permission_classes
from rest_framework import viewsets, permissions, status
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.utils.crypto import get_random_string
from send_email.views import SendEmail
from .serializers import *
from .models import *
from accounts.models import *

# Create your views here.

class ReceiptViewSet(viewsets.ModelViewSet):
	permission_classes = (AllowAny,)
	serializer_class = ReceiptSerializer
	queryset = Service.objects.all()

	def create(self, request):
		user = request.data.get('user', None)
		receipt = request.data.get('receipt', None)
		total = request.data.get('total', None)

		# get user
		user_instance = get_object_or_404(User.objects.all(), id=user['id'])
		# service names
		service_names = []
		for service in receipt:
			service_names.append(service['name'])
		# get service names from model
		service_queryset = Service.objects.filter(name__in=service_names)
		# create recipt intance
		receipt_instance = Receipt.objects.create(user=user_instance, total=total)
		# add services to receipt
		for service in list(service_queryset):
			receipt_instance.service.add(service)

		return Response(status=status.HTTP_201_CREATED)


