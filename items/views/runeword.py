from rest_framework import viewsets, filters

from items.models import Runeword
from items.serializers import RunewordSerializer


class RunewordsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Runeword.objects.all()
    serializer_class = RunewordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'common_name', 'runes__name', 'statistics')
