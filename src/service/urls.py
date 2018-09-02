from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

# order matters
router.register(r'', ReceiptViewSet, base_name='receipt'),


urlpatterns = [
    url(r'^', include(router.urls))
]