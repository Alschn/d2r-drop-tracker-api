from django import forms
from django.contrib import admin
from django.db.models import QuerySet
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from ordered_model.admin import OrderedModelAdmin

from common.admin import ModelAdmin, ModelResourceWithNestedJSON
from .models import (
    Set, ItemInSet, Runeword, Item, ItemBase, ItemQuality, ConcreteItem, Jewelry, Rune, Charm, Jewel,
    Miscellaneous, RuneInRuneword, ConcreteRuneword, ItemType
)


class ItemBaseAdminForm(forms.ModelForm):
    type = forms.ChoiceField(
        choices=list(map(lambda x: (x.value, x.label), ItemType.socketables()))
    )
    quality = forms.ChoiceField(
        choices=((ItemQuality.NORMAL.value, ItemQuality.NORMAL.label),)
    )

    class Meta:
        model = ItemBase
        fields = "__all__"


@admin.register(ItemBase)
class ItemBaseAdmin(ImportExportModelAdmin, ModelAdmin):
    form = ItemBaseAdminForm
    list_display = (
        'name', 'type', 'level_type',
        'str_req', 'dex_req', 'level_req', 'max_sockets',
        'class_specific',
    )
    list_filter = ('type', 'max_sockets', 'class_specific')
    ordering = ('type',)


@admin.register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ('name', 'quality', 'type', 'level_req')
    list_filter = ('quality', 'type')

    def has_add_permission(self, *args, **kwargs):
        return False


class ConcreteItemAdminForm(forms.ModelForm):
    class Meta:
        model = ConcreteItem
        fields = "__all__"


@admin.register(ConcreteItem)
class ConcreteItemAdmin(ModelAdmin):
    list_filter = ('quality', 'type')


class RunewordAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Runeword
        fields = "__all__"


class RunewordResource(ModelResourceWithNestedJSON):
    class Meta:
        model = Runeword
        exclude = ('runes',)


@admin.register(Runeword)
class RunewordAdmin(ImportExportModelAdmin, ModelAdmin):
    form = RunewordAdminForm
    resource_class = RunewordResource


class RuneInRunewordResource(resources.ModelResource):
    runeword = fields.Field(
        column_name="runeword_id",
        attribute="runeword",
        widget=ForeignKeyWidget(Runeword)
    )
    rune = fields.Field(
        column_name="rune_id",
        attribute="rune",
        widget=ForeignKeyWidget(Rune)
    )

    class Meta:
        model = RuneInRuneword
        fields = ("id", "order", "runeword", "rune")


@admin.register(RuneInRuneword)
class RuneInRunewordAdmin(ImportExportModelAdmin, OrderedModelAdmin):
    list_select_related = ("runeword", "rune")
    list_display = ("__str__", "order", "move_up_down_links")
    ordering = ('runeword', 'order',)
    resource_class = RuneInRunewordResource


@admin.register(ConcreteRuneword)
class ConcreteRunewordAdmin(admin.ModelAdmin):
    pass


class ItemInSetAdminForm(forms.ModelForm):
    item = forms.ModelChoiceField(
        queryset=Item.objects.none()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].queryset = ConcreteItem.objects.filter(quality=ItemQuality.SET)

    class Meta:
        model = ItemInSet
        fields = "__all__"


@admin.register(ItemInSet)
class ItemInSetAdmin(admin.ModelAdmin):
    form = ItemInSetAdminForm
    list_select_related = ("set", "item")
    list_display = ('__str__', 'set')


class SetResource(ModelResourceWithNestedJSON):
    class Meta:
        model = Set
        exclude = ('parts',)


@admin.register(Set)
class SetAdmin(ImportExportModelAdmin, ModelAdmin):
    list_filter = ('level_type',)
    resource_class = SetResource


# Proxies
class ItemResource(ModelResourceWithNestedJSON):
    class Meta:
        model = Item


class JewelryAdminForm(forms.ModelForm):
    type = forms.ChoiceField(
        choices=list(map(lambda x: (x.value, x.label), ItemType.jewelry()))
    )
    quality = forms.ChoiceField(
        choices=(
            (ItemQuality.MAGIC.value, ItemQuality.MAGIC.label),
            (ItemQuality.RARE.value, ItemQuality.RARE.label),
            (ItemQuality.CRAFTED.value, ItemQuality.CRAFTED.label),
            (ItemQuality.UNIQUE.value, ItemQuality.UNIQUE.label),
        )
    )

    class Meta:
        model = Rune
        fields = "__all__"


@admin.register(Jewelry)
class JewelryAdmin(ModelAdmin):
    form = JewelryAdminForm
    resource_class = ItemResource


class RuneAdminForm(forms.ModelForm):
    type = forms.ChoiceField(
        choices=((ItemType.RUNE.value, ItemType.RUNE.label),)
    )
    quality = forms.ChoiceField(
        choices=((ItemQuality.NORMAL.value, ItemQuality.NORMAL.label),)
    )

    class Meta:
        model = Rune
        fields = "__all__"


class RuneLevelFilter(admin.SimpleListFilter):
    title = "Rune's level"
    parameter_name = "level_req"

    def lookups(self, request, model_admin):
        return (
            ("high", "High Rune"),
            ("mid", "Mid Rune"),
            ("low", "Low Rune"),
        )

    def queryset(self, request, queryset) -> QuerySet[Rune]:
        value = self.value()
        if value == "high":
            return queryset.filter(level_req__gte=55)
        elif value == "mid":
            return queryset.filter(level_req__gte=39, level_req__lt=55)
        elif value == "low":
            return queryset.filter(level_req__lt=39)


@admin.register(Rune)
class RuneAdmin(ImportExportModelAdmin, ModelAdmin):
    form = RuneAdminForm
    list_display = ('name', 'level_req')
    list_filter = (RuneLevelFilter,)
    resource_class = ItemResource


class CharmAdminForm(forms.ModelForm):
    type = forms.ChoiceField(
        choices=((ItemType.CHARM.value, ItemType.CHARM.label),)
    )
    quality = forms.ChoiceField(
        choices=(
            (ItemQuality.MAGIC.value, ItemQuality.MAGIC.label),
            (ItemQuality.UNIQUE.value, ItemQuality.UNIQUE.label),
        )
    )

    class Meta:
        model = Charm
        fields = "__all__"


@admin.register(Charm)
class CharmAdmin(ModelAdmin):
    form = CharmAdminForm
    resource_class = ItemResource


class JewelAdminForm(forms.ModelForm):
    type = forms.ChoiceField(
        choices=((ItemType.JEWEL.value, ItemType.JEWEL.label),)
    )
    quality = forms.ChoiceField(
        choices=(
            (ItemQuality.MAGIC.value, ItemQuality.MAGIC.label),
            (ItemQuality.RARE.value, ItemQuality.RARE.label),
            (ItemQuality.UNIQUE.value, ItemQuality.UNIQUE.label),
        )
    )

    class Meta:
        model = Jewel
        fields = "__all__"


@admin.register(Jewel)
class JewelAdmin(ModelAdmin):
    form = JewelAdminForm
    resource_class = ItemResource


class MiscellaneousAdminForm(forms.ModelForm):
    type = forms.ChoiceField(
        choices=list(map(lambda x: (x.value, x.label), ItemType.miscellaneous()))
    )
    quality = forms.ChoiceField(
        choices=((ItemQuality.NORMAL.value, ItemQuality.NORMAL.label),)
    )

    class Meta:
        model = Miscellaneous
        fields = "__all__"


@admin.register(Miscellaneous)
class MiscellaneousAdmin(ImportExportModelAdmin, ModelAdmin):
    form = MiscellaneousAdminForm
    list_display = ("name", "type", "level_req")
    resource_class = ItemResource
