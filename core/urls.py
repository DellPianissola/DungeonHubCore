from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.user.api.views import UserViewSet


router = DefaultRouter()
router.register('user', UserViewSet)

app_name = 'core'


urlpatterns  = [
    path('', include(router.urls))
]