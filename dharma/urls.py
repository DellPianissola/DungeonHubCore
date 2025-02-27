from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dharma.nature.api.views import NatureViewSet
from dharma.technique.api.views import TechniqueViewSet


router = DefaultRouter()
router.register('nature', NatureViewSet, basename='nature')
router.register('technique', TechniqueViewSet, basename='technique')


app_name = 'dharma'


urlpatterns  = [
    path('', include(router.urls))
]