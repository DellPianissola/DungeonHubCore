from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from dharma.weapon.api.serializer import WeaponSerializer
from dharma.weapon.models.weapon import Weapon


@extend_schema(tags=["Dharma - Weapon"])
class WeaponViewSet(viewsets.ModelViewSet):

    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
