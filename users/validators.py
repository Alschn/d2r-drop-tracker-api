from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UnicodeBattleNetUsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+(#\d+)?\Z"
    message = _(
        "Enter a valid username. This value may contain only letters, "
        "numbers, and @/./+/-/_ characters and optionally include battletag at the end."
    )
