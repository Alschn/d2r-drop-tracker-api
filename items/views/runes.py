from rest_framework import viewsets, filters

from items.models import Rune
from items.serializers import RuneSerializer


class RunesViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Rune.objects.all()
    serializer_class = RuneSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'common_name',)
