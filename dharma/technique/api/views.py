from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from dharma.technique.api.serializer import TechniqueSerializer
from dharma.technique.models.technique import Technique


@extend_schema(tags=["Dharma - Technique"])
class TechniqueViewSet(viewsets.ModelViewSet):

    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer
