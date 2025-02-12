from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('user', UserViewSet, basename='user')

app_name = 'dharma'


urlpatterns  = [
    path('', include(router.urls))
]