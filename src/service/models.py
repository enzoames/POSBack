from django.db import models
from django.contrib.postgres.fields import JSONField
from accounts.models import User


class Service(models.Model):
	name = models.CharField(max_length=140, blank=True, null=True)
	price = models.DecimalField(default=0, decimal_places=2, max_digits=9, verbose_name='Price')

	def __str__(self):
		return str(self.id) + ' ' + self.name + ' ' + str(self.price)
	

class Receipt(models.Model):
	user = models.ForeignKey(User, related_name='user_handled_service', blank=True, null=True, on_delete=models.CASCADE)
	service = models.ManyToManyField(Service, related_name='user_service_done', blank=True)
	total = models.DecimalField(default=0, decimal_places=2, max_digits=9, verbose_name='Total')
	created_at = models.DateField(auto_now_add=True, blank=True, null=True)
	created_time_at = models.TimeField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id) + ' ' + self.user.first_name + ' ' + str(self.total)
	
	def get_services(self):
		return ",\n".join([service.name for service in self.service.all()])