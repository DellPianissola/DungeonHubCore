from rest_framework import serializers

from dharma.weapon.models.weapon import Weapon


class WeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = ['id', 'name', 'damage', 'description', 'image']
