from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from items.models import Item
from items.serializers import ItemSerializer


class ItemsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('type', 'quality')
    search_fields = ('name', 'common_name', 'type', 'quality', 'statistics')
