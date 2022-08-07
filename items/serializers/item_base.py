from rest_framework import serializers

from items.models import ItemBase


class ItemBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBase
        fields = "__all__"
