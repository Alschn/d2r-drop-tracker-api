from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Character(models.Model):
    class Class(models.TextChoices):
        AMAZON = "amazon", "Amazon"
        BARBARIAN = "barbarian", "Barbarian"
        NECROMANCER = "necromancer", "Necromancer"
        PALADIN = "paladin", "Paladin"
        SORCERESS = "sorceress", "Sorceress"
        DRUID = "druid", "Druid"
        ASSASSIN = "assassin", "Assassin"

    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    name = models.CharField(max_length=15)
    level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)]
    )
    char_class = models.CharField(choices=Class.choices, max_length=11)

    expansion = models.BooleanField(default=True, blank=True)
    hardcore = models.BooleanField(default=False, blank=True)
    ladder = models.BooleanField(default=False, blank=True)

    # todo inventory, stash, cube + merc

    def __str__(self) -> str:
        return f"{self.name} level {self.level}"
