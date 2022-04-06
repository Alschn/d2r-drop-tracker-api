from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from areas.models import Area, Difficulty
from characters.models import Character


class Sellable(models.Model):
    sold_for = models.DecimalField(
        max_digits=7, decimal_places=2,
        blank=True, null=True,
        validators=[MinValueValidator(Decimal(0.01))]
    )
    sold_at = models.DateTimeField(blank=True, null=True)
    sold_to = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True


class ItemFind(Sellable):
    item = models.ForeignKey(to="items.Item", on_delete=models.CASCADE)
    statistics = models.JSONField(blank=True, null=True, default=dict)

    found_by = models.ForeignKey(to=Character, on_delete=models.SET_NULL, blank=True, null=True)
    found_at = models.DateTimeField(blank=True, null=True)
    found_in = models.ForeignKey(to=Area, on_delete=models.SET_NULL, blank=True, null=True)
    found_on_difficulty = models.CharField(max_length=9, choices=Difficulty.choices, blank=True, null=True)
    found_on_players = models.PositiveIntegerField(blank=True, null=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(8)
    ])

    def __str__(self) -> str:
        return f"{self.item.name}"
