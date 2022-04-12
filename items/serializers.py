from rest_framework import serializers

from items.models import ItemBase, Rune, Runeword, Item, ConcreteItem


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"


class ConcreteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcreteItem
        fields = "__all__"


class ItemBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBase
        fields = "__all__"


class RuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rune
        fields = "__all__"


class EmbeddedRuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rune
        fields = (
            'id', 'name', "level_req", "statistics"
        )


class RunewordSerializer(serializers.ModelSerializer):
    runes = EmbeddedRuneSerializer(many=True)

    class Meta:
        model = Runeword
        fields = "__all__"
