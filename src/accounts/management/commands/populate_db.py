"""

IMPORTANT!

THIS IS WHERE WE POPULATE OUR DATABASE
FOR DEVELOPMENT PURPOSES ONLY

"""
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from accounts.models import *
from service.models import *

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def _populate(self):
		print ('POPULATING')
		service_list = [
			{
				'name': 'Manicure',
				'price': 7,
			},
			{
				'name': 'French Manicure',
				'price': 13,
			},
			{
				'name': 'Polish Change',
				'price': 8,
			},
			{
				'name': 'Dip Powder',
				'price': 30,
			},
			{
				'name': 'French Dip Powder',
				'price': 35,
			},
			{
				'name': 'Mani Pedi Combo',
				'price': 25,
			},
			{
				'name': 'Regulart Pedicure',
				'price': 20,
			},
			{
				'name': 'Polish Charge',
				'price': 10,
			},
			{
				'name': 'Callus Remover',
				'price': 10,
			},
			{
				'name': 'Dip Powder & Tips',
				'price': 10,
			},
			{
				'name': 'Kids Manu Pedi',
				'price': 15,
			},
			{
				'name': 'Gel Color',
				'price': 20,
			},
			{
				'name': 'Gel French',
				'price': 25,
			},
			{
				'name': 'Polish Change',
				'price': 13,
			},
			{
				'name': 'Gel Soak',
				'price': 6,
			},
			{
				'name': 'UV Gel',
				'price': 6,
			},
			{
				'name': 'UV Gel Soak',
				'price': 6,
			},
			{
				'name': 'Eyebrows',
				'price': 5,
			},
			{
				'name': 'Upper Lip',
				'price': 5,
			},
			{
				'name': 'Lower Lip',
				'price': 3,
			},
			{
				'name': 'Chin',
				'price': 5,
			},
			{
				'name': 'Forehead',
				'price': 5,
			},
			{
				'name': 'Neck',
				'price': 5,
			},
			{
				'name': 'Side Face',
				'price': 10,
			},
			{
				'name': 'Full Face',
				'price': 26,
			},
			{
				'name': 'Nose',
				'price': 5,
			},
			{
				'name': 'Under Arms',
				'price': 10,
			},
			{
				'name': 'Full Arms',
				'price': 20,
			},
			{
				'name': 'Half Arms',
				'price': 17,
			},
			{
				'name': 'Half Legs',
				'price': 20,
			},
			{
				'name': 'Full Legs',
				'price': 35,
			},
			{
				'name': 'Chest',
				'price': 30,
			},
			  {
				'name': 'Aroma',
				'price': 50,
			},
			{
				'name': 'Onsen',
				'price': 50,
			},
			{
				'name': 'Chamomile',
				'price': 50,
			},
			{
				'name': 'Green Tea',
				'price': 60,
			},
			{
				'name': 'Pearl',
				'price': 60,
			},
			{
				'name': 'Reflexology',
				'price': 30,
			},
			{
				'name': 'Arcrylic & Gel Polish',
				'price': 50,
			},
			{
				'name': 'Arcrylic & Reg. Polish',
				'price': 50,
			},
			{
				'name': 'Arcrylic Soak',
				'price': 50,
			},
		]
		
		for service in service_list:
			Service.objects.create(name=service['name'], price=service['price'])

		print ('DONE')

	# =======================================
	# =========== HANDLE FUNCTION ===========
	# =======================================

	def handle(self, *args, **options):
		self._populate()
		# print ("NO NEED TO POPULATE DATABASE")
