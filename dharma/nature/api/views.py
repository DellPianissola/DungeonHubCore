from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from dharma.nature.api.serializer import NatureSerializer
from dharma.nature.models.nature import Nature


@extend_schema(tags=["Dharma - Nature"])
class NatureViewSet(viewsets.ModelViewSet):

    queryset = Nature.objects.all()
    serializer_class = NatureSerializer