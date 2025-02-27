from rest_framework import serializers

from dharma.technique.models.technique import Technique


class TechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Technique
        fields = ['id', 'name', 'xp_cost', 'type', 'requirements', 'effect', 'description', 'image']
