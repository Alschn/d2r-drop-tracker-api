from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ordered_model.models import OrderedModel


class Difficulty(models.TextChoices):
    NORMAL = "normal", "Normal"
    NIGHTMARE = "nightmare", "Nightmare"
    HELL = "hell", "Hell"


class Area(OrderedModel):
    class Act(models.IntegerChoices):
        A1 = "1", "Rogue Encampment"
        A2 = "2", "Lut Gholein"
        A3 = "3", "Kurast Docks"
        A4 = "4", "Pandemonium Fortress"
        A5 = "5", "Harrogath"

    name = models.CharField(max_length=60, unique=True)
    act = models.PositiveIntegerField(choices=Act.choices)
    normal_level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(43)]
    )
    nightmare_level = models.PositiveIntegerField(
        validators=[MinValueValidator(36), MaxValueValidator(66)]
    )
    hell_level = models.PositiveIntegerField(
        validators=[MinValueValidator(67), MaxValueValidator(87)]
    )

    order_with_respect_to = "act"

    def __str__(self) -> str:
        return f"A{self.act} {self.name}"
