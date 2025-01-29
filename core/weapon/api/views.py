from rest_framework import viewsets

from core.weapon.api.serializer import WeaponSerializer
from core.weapon.models.weapon import Weapon


class WeaponViewSet(viewsets.ModelViewSet):

    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer