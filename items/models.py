from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import QuerySet
from ordered_model.models import OrderedModel

from characters.models import Character

MAX_STR_REQUIRED = 253  # thunder maul
MAX_DEX_REQUIRED = 167  # hydra bow


class ItemQuality(models.TextChoices):
    LOW = "low", "Low"
    NORMAL = "normal", "Normal"
    SUPERIOR = "superior", "Superior"
    MAGIC = "magic", "Magic"
    RARE = "rare", "Rare"
    CRAFTED = "crafted", "Crafted"
    SET = "set", "Set"
    UNIQUE = "unique", "Unique"


class ItemType(models.TextChoices):
    ARMOR = "armor", "Armor"
    BELT = "belt", "Belt"
    BOOTS = "boots", "Boots"
    GLOVES = "gloves", "Gloves"
    HELMET = "helmet", "Helmet"
    HELM = "barb_helm", "Barbarian's Helm"
    PELT = "druid_pelt", "Druid's Pelt"
    SHIELD = "shield", "Shield"
    AURIC_SHIELD = "auric_shield", "Paladin's Shield"
    NECRO_HEAD = "shrunken_head", "Necromancer's Shrunken Head"
    AXE_1H = "axe_1h", "One-handed Axe"
    AXE_2H = "axe_2h", "Two-handed Axe"
    KATAR = "katar", "Assassin's Claw"
    DAGGER = "dagger", "Dagger"
    SWORD_1H = "sword_1h", "One-handed Sword"
    SWORD_2H = "sword_2h", "Two-handed Sword"
    HAMMER = "hammer", "Hammer"
    MAUL = "maul", "Maul"
    MACE = "mace", "Mace"
    CLUB = "club", "Club"
    SCEPTER = "scepter", "Scepter"
    POLEARM = "polearm", "Polearm"
    AMAZON_SPEAR = "amazon_spear", "Amazon's Spear"
    SPEAR = "spear", "Spear"
    WAND = "wand", "Wand"
    STAFF = "staff", "Staff"
    ORB = "orb", "Sorceress' Orb"
    CROSSBOW = "crossbow", "Crossbow"
    AMAZON_BOW = "amazon_bow", "Amazon's Bow"
    BOW = "bow", "Bow"
    THROWING = "throwing", "Throwing"
    AMAZON_JAVELIN = "amazon_javelin", "Amazon's Javelin"
    JAVELIN = "javelin", "Javelin"
    RING = "ring", "Ring"
    AMULET = "amulet", "Amulet"
    GEM = "gem", "Gem"
    RUNE = "rune", "Rune"
    CHARM = "charm", "Charm"
    JEWEL = "jewel", "Jewel"
    SCROLL = "scroll", "Scroll"
    TOME = "tome", "Tome"
    AMMO = "ammo", "Ammunition"
    POTION = "potion", "Potion"
    KEY = "key", "Key"
    QUEST = "quest", "Quest"

    @classmethod
    def socketables(cls) -> list["ItemType"]:
        return [
            cls.HELMET, cls.HELM, cls.PELT, cls.ARMOR, cls.SHIELD, cls.AURIC_SHIELD, cls.NECRO_HEAD, cls.AXE_1H,
            cls.AXE_2H, cls.KATAR, cls.DAGGER, cls.SWORD_1H, cls.SWORD_2H, cls.HAMMER, cls.MAUL, cls.MACE,
            cls.CLUB, cls.SCEPTER, cls.POLEARM, cls.SPEAR, cls.WAND, cls.STAFF, cls.ORB, cls.CROSSBOW,
            cls.BOW, cls.AMAZON_BOW, cls.AMAZON_SPEAR
        ]

    @classmethod
    def jewelry(cls) -> list["ItemType"]:
        return [cls.RING, cls.AMULET]

    @classmethod
    def miscellaneous(cls) -> list["ItemType"]:
        return [
            cls.GEM, cls.POTION, cls.QUEST,
            cls.KEY, cls.TOME, cls.AMMO,
        ]


class ItemLevelType(models.TextChoices):
    NORMAL = "normal", "normal"
    EXCEPTIONAL = "exceptional", "exceptional"
    ELITE = "elite", "elite"


class GenericItem(models.Model):
    name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=20, blank=True, null=True)
    level_req = models.PositiveIntegerField(
        blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(99)]
    )
    statistics = models.JSONField(blank=True, null=True, default=dict)

    class Meta:
        abstract = True


class TypeQualityItem(GenericItem):
    type = models.CharField(max_length=14, choices=ItemType.choices)
    quality = models.CharField(max_length=8, choices=ItemQuality.choices)

    class Meta:
        abstract = True


class Item(TypeQualityItem):
    pass

    def __str__(self) -> str:
        return f"{self.name} {self.quality} {self.type}"


class ItemBase(TypeQualityItem):
    max_sockets = models.PositiveIntegerField(
        default=0,
        blank=True, null=True,
        validators=[MinValueValidator(0), MaxValueValidator(6)],
    )
    level_type = models.CharField(max_length=11, choices=ItemLevelType.choices)
    class_specific = models.CharField(
        max_length=12, choices=Character.Class.choices,
        blank=True, null=True
    )
    str_req = models.PositiveIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(MAX_STR_REQUIRED)]
    )
    dex_req = models.PositiveIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(MAX_DEX_REQUIRED)]
    )
    durability = models.PositiveIntegerField(
        blank=True, null=True, validators=[
            MaxValueValidator(255)
        ]
    )

    def __str__(self) -> str:
        return f"{self.name} {self.quality} {self.type}"

    @property
    def is_socketable(self) -> bool:
        return bool(self.max_sockets)


class JewelryManager(models.Manager):
    def get_queryset(self) -> QuerySet[Item]:
        return Item.objects.filter(
            type__in=[ItemType.RING, ItemType.AMULET]
        )


class Jewelry(Item):
    objects = JewelryManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Jewelry"


class RuneManager(models.Manager):

    def get_queryset(self) -> QuerySet[Item]:
        return Item.objects.filter(
            type=ItemType.RUNE
        )


class Rune(Item):
    objects = RuneManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Runes"


class CharmsManager(models.Manager):
    def get_queryset(self) -> QuerySet[Item]:
        return Item.objects.filter(
            type=ItemType.CHARM
        )


class Charm(Item):
    objects = CharmsManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Charms"


class JewelsManager(models.Manager):
    def get_queryset(self) -> QuerySet[Item]:
        return Item.objects.filter(
            type=ItemType.JEWEL
        )


class Jewel(Item):
    objects = JewelsManager()

    class Meta:
        proxy = True


class MiscellaneousManager(models.Manager):
    def get_queryset(self) -> QuerySet[Item]:
        return Item.objects.filter(
            type__in=ItemType.miscellaneous()
        )


class Miscellaneous(Item):
    objects = MiscellaneousManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Miscellaneous items"


class ConcreteItem(Item):
    base = models.ForeignKey(to=ItemBase, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        if not self.base:
            return f"{self.name} {self.quality} {self.type}"

        return f"{self.name} {self.quality} {self.base.name} {self.type}"


class SetItemManager(models.Manager):
    def get_queryset(self) -> QuerySet['ConcreteItem']:
        return ConcreteItem.objects.filter(quality=ItemQuality.SET)


class SetItem(ConcreteItem):
    objects = SetItemManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Set items"


class UniqueItemManager(models.Manager):
    def get_queryset(self) -> QuerySet['ConcreteItem']:
        return ConcreteItem.objects.filter(quality=ItemQuality.UNIQUE)


class UniqueItem(ConcreteItem):
    objects = UniqueItemManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Unique items"


class ConcreteRuneword(models.Model):
    base = models.ForeignKey(to=ItemBase, on_delete=models.CASCADE)
    runeword = models.ForeignKey(to="Runeword", on_delete=models.SET_NULL, blank=True, null=True)
    statistics = models.JSONField(blank=True, null=True, default=dict)

    def __str__(self) -> str:
        # careful! runeword can be null
        return f"{self.runeword.name} in {self.base.name}"


class RuneInRuneword(OrderedModel):
    rune = models.ForeignKey(to=Rune, on_delete=models.CASCADE)
    runeword = models.ForeignKey(to="Runeword", on_delete=models.CASCADE)

    order_with_respect_to = "runeword"

    class Meta:
        verbose_name_plural = "Runes in Runeword"

    def __str__(self) -> str:
        return f"{self.rune.name} - {self.runeword.name}"


class Runeword(models.Model):
    name = models.CharField(max_length=100, unique=True)
    common_name = models.CharField(max_length=20, blank=True, null=True)
    level_req = models.PositiveIntegerField(
        blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(99)]
    )
    statistics = models.JSONField(blank=True, null=True, default=dict)
    runes = models.ManyToManyField(
        to=Rune, through=RuneInRuneword,
        through_fields=('runeword', 'rune'),
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class ItemInSet(models.Model):
    item = models.ForeignKey(to=ConcreteItem, on_delete=models.CASCADE)
    set = models.ForeignKey(to="Set", on_delete=models.CASCADE)
    bonus = models.JSONField(blank=True, null=True, default=dict)

    class Meta:
        verbose_name_plural = "Items in Set"

    def __str__(self) -> str:
        return self.item.name


class Set(models.Model):
    name = models.CharField(max_length=100)
    level_type = models.CharField(max_length=11, choices=ItemLevelType.choices)
    parts = models.ManyToManyField(
        to=ConcreteItem, through=ItemInSet,
        through_fields=('set', 'item'),
        blank=True
    )
    bonus = models.JSONField(blank=True, null=True, default=dict)

    def __str__(self) -> str:
        return f"{self.name} Set"
