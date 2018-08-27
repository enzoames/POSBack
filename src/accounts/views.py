from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import *
from .serializers import *


# ============================================
# ======= SPORTA REGISTRATION VIEW SET =======
# ============================================
# This is used duing on boarding, after the user's email has been verified

class SportaRegistrationViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated, )
	queryset = User.objects.all()
	serializer_class = SportaRegistrationSerializer

	# =======================================
	# ======= UPDATE USER INFORMATION =======
	# =======================================

	def put(self, request, format=None):
		if request.user is not None:
			data = {
	            'first_name': request.data.get('firstName', None),
	            'last_name': request.data.get('lastName', None),
	            'credential': request.data.get('credential', None),
	            'username': request.data.get('username', None),
	        }

			serializer = SportaRegistrationSerializer(data=data)
			if serializer.is_valid():
				user_instance, athlete_instance = serializer.update(request.user, serializer.validated_data)

				# check pending invitations
				if UserPendingInvitation.objects.filter(email=request.user.email).exists():
					invitations = UserPendingInvitation.objects.filter(email=request.user.email).select_related('team_invitation__athlete', 'league_invitation__athlete')
					print ('[1] invitations', invitations)
					for invitation in list(invitations):
						if invitation.league_invitation is not None:
							invitation.league_invitation.athlete = athlete_instance
							invitation.league_invitation.save()
							print ('[2] league invitaion updated')
						elif invitation.team_invitation is not None:
							invitation.team_invitation.athlete = athlete_instance
							invitation.team_invitation.save()
							print ('[2] team invitaion updated')
					
					invitations.delete()
					# User has new notification
					user_instance.has_notification = True 
					user_instance.save()
					print ('[3]')
				return Response(model_to_dict(user_instance, exclude=['password']), status=status.HTTP_201_CREATED)
			else:
				return Response({'error': 'couldnt update'}, status = status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'error': 'Unable to Verify'}, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self, request, pk=None):
		print (request.user)
		if request.user and pk:
			request.user.is_active = False
			request.user.save()
			# send email to user that his account is deactivated
			return Response({'detail': 'success'}, status=status.HTTP_200_OK)
		else:
			return Response({'error': 'invalid [0]'}, status=status.HTTP_400_BAD_REQUEST)



