from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dharma.nature.api.views import NatureViewSet


router = DefaultRouter()
router.register('nature', NatureViewSet, basename='nature')


app_name = 'dharma'


urlpatterns  = [
    path('', include(router.urls))
]