from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# router.register(r'user', UserBasicInfoViewSet, base_name='alluser_instances')

urlpatterns = [
    url(r'^', include(router.urls)),
]
