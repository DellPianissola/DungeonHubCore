from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dharma.nature.api.views import NatureViewSet
from dharma.technique.api.views import TechniqueViewSet
from dharma.weapon.api.views import WeaponViewSet


router = DefaultRouter()
router.register('nature', NatureViewSet, basename='nature')
router.register('technique', TechniqueViewSet, basename='technique')
router.register('weapon', WeaponViewSet, basename='weapon')


app_name = 'dharma'


urlpatterns  = [
    path('', include(router.urls))
]