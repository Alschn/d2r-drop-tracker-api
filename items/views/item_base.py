from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from items.models import ItemBase
from items.serializers import ItemBaseSerializer


class ItemBasesViewset(viewsets.ReadOnlyModelViewSet):
    queryset = ItemBase.objects.all()
    serializer_class = ItemBaseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = (
        'type', 'level_type', 'max_sockets', 'class_specific',
    )
    search_fields = ('name', 'common_name', 'statistics')
    ordering_fields = ('str_req', 'dex_req', 'level_req', 'name', 'id')
