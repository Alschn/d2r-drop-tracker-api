from rest_framework import serializers

from items.models import Runeword
from items.serializers import EmbeddedRuneSerializer


class RunewordSerializer(serializers.ModelSerializer):
    runes = EmbeddedRuneSerializer(many=True)

    class Meta:
        model = Runeword
        fields = "__all__"
