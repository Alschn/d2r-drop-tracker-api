from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import ItemBase, Rune, Runeword, Item
from .serializers import ItemBaseSerializer, RuneSerializer, RunewordSerializer, ItemSerializer


class ItemsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('type', 'quality')
    search_fields = ('name', 'common_name', 'type', 'quality', 'statistics')


class ItemBasesViewset(viewsets.ReadOnlyModelViewSet):
    queryset = ItemBase.objects.all()
    serializer_class = ItemBaseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = (
        'type', 'level_type', 'max_sockets', 'class_specific',
    )
    search_fields = ('name', 'common_name', 'statistics')
    ordering_fields = ('str_req', 'dex_req', 'level_req', 'name', 'id')


class RunesViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Rune.objects.all()
    serializer_class = RuneSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'common_name',)


class RunewordsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Runeword.objects.all()
    serializer_class = RunewordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'common_name', 'runes__name', 'statistics')
