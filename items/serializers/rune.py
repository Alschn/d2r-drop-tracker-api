from rest_framework import serializers

from items.models import Rune


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
