from rest_framework import viewsets
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from accounts.models import *
#import datetime

class SendEmail(object):
	def __init__(self):
		self.url = 'https://clubsporta.com/'
		self.company_name = 'SPORTA'
		self.from_email = 'sporta@clubsporta.com'
		# self.cc = ['plugr@zahncenternyc.com']
		self.cc = ['']

	def release_email(self, sub, body, frm, to, cc=None):
		constructing_email = EmailMessage(sub, body, frm, to, cc=cc)
		constructing_email.send()

	def send_confirm_registration(self, new_registered_user, token):
		subject = '[SPORTA] Thank you for registering!'
		body = 'Please confirm your email to continue with your registration by going to the following link ' + 'localhost:7000/register/confirmation/' + token
		self.release_email(subject, body, self.from_email, [new_registered_user], self.cc)

	def send_new_athlete_team_invitation(self, new_athlete_email, team_name, league_name, token):
		subject = "[SPORTA] You've been invited to join " + team_name + ' from ' + league_name
		body = 'Follow the link below to join! localhost:7000/register/athlete - If you think we reached the wrong person, contact us or simply remove your email from our system by clicking localhost:7000/invalidinviatation/athlete/' + token
		self.release_email(subject, body, self.from_email, [new_athlete_email], self.cc)

	def send_new_athlete_team_invitation_no_league(self, new_athlete_email, team_name, token):
		subject = "[SPORTA] You've been invited to join " + team_name
		body = 'Follow the link below to join! localhost:7000/register/athlete - If you think we reached the wrong person, contact us or simply remove your email from our system by clicking localhost:7000/invalidinviatation/athlete/' + token
		self.release_email(subject, body, self.from_email, [new_athlete_email], self.cc)

	def send_captain_invitation(self, new_captain_email, league_name, token):
		subject = "[SPORTA] You've been invited to become a team captain and join " + league_name
		body = 'Follow the link below to join! localhost:7000/register/team - If you think we reached the wrong person, contact us or simply remove your email from our system by clicking localhost:7000/invalidinviatation/team/' + token
		self.release_email(subject, body, self.from_email, [new_captain_email], self.cc)

	def send_new_athlete_team_division_invitation(self, new_athlete_email, from_athlete_name, team_name, division_name, league_name, token):
		subject = '[SPORTA] ' + from_athlete_name + ' is inviting you to join ' + team_name
		body = team_name + ' will play in ' +  division_name + ' for ' + league_name + '. Follow the link below to join! localhost:7000/register/athlete - If you think we reached the wrong person, contact us or simply remove your email from our system by clicking localhost:7000/invalidinviatation/athlete/' + token
		self.release_email(subject, body, self.from_email, [new_athlete_email], self.cc)

	def send_team_manager_new_contact_message(self, to_email_list, from_user, message):
		subject = '[SPORTA] Your team has a new message'
		body = 'You have received a new message from ' + from_user.first_name + ' ' + from_user.last_name + ", '"+ message + "'. You can reach out to him at " + from_user.email + ' or visit his profile at clubsporta.com/profile/athlete/' + from_user.username + ' Thank you ! - Sporta Team'
		self.release_email(subject, body, self.from_email, to_email_list, self.cc)