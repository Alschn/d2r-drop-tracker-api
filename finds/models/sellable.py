from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


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
