from rest_framework import serializers

from items.models import Item, ConcreteItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ConcreteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcreteItem
        fields = "__all__"
