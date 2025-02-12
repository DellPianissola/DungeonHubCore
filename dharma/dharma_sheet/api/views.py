from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from core.user.api.serializer import UserSerializer
from core.user.models.user import User


@extend_schema(tags=["Core - User"])
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer