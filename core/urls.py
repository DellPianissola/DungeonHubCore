from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.weapon.api.views import WeaponViewSet


router = DefaultRouter()
router.register('weapon', WeaponViewSet)

app_name = 'core'


urlpatterns  = [
    path('', include(router.urls))
]