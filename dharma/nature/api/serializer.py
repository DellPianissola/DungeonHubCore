from rest_framework import serializers

from dharma.nature.models.nature import Nature


class NatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nature
        fields = ['id', 'name', 'points', 'description', 'image']
