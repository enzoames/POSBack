from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.crypto import get_random_string
from send_email.views import SendEmail
from django.utils.translation import ugettext_lazy as _
#from django.contrib.postgres.fields import JSONField

# ================================
# ========= USER MANAGER =========
# ================================
# Used when creating new super users 

class UserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is 'UserManager'
    """
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        print ('\n\nCREATING USER HERE')
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class EmailLoginField(models.EmailField):
	def get_prep_value(self, value):
		if value == '':
			return None
		return value


# ==============================
# ========= USER MODEL =========
# ==============================
# The most important model

class User(AbstractBaseUser, PermissionsMixin):
	credential_choices = ( ('M', 'Manager'), ('ADMIN', 'ADMIN') )

	email = EmailLoginField(max_length=100, unique=True, null=True, blank=True, verbose_name='Email Address')
	username = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='Username')
	first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='First Name')
	last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Last Name')
	joined = models.DateTimeField(auto_now_add=True)
	date_of_birth = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
	is_active = models.BooleanField(default=False, verbose_name='Is active ?') # users must confirm email in order to become active
	is_admin = models.BooleanField(default=False, verbose_name='Is admin ?')
	is_staff = models.BooleanField(default=False, verbose_name='Is staff ?')
	credential = models.CharField(max_length=30, choices=credential_choices, null=True,blank=True, verbose_name='Credential')
	has_notification = models.BooleanField(default=False, verbose_name='Has notification ?')
	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	#region = JSONField(default=dict, blank=True, null=True, verbose_name='Region', help_text='json field containining city, state, country')
	USERNAME_FIELD = 'email'
	objects = UserManager()
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def get_username(self):
		if not self.email:
			return 'self'
		else:
			return self.email
