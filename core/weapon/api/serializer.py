from rest_framework import serializers

from core.weapon.models.weapon import Weapon


class WeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = ("id", "name", "damage", "description")