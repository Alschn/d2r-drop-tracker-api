from django import forms
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
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
class ItemBaseAdmin(ModelAdmin):
    form = ItemBaseAdminForm
    list_filter = ('type',)


@admin.register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ('__str__', 'name', 'quality', 'type')
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


@admin.register(RuneInRuneword)
class RuneInRunewordAdmin(OrderedModelAdmin):
    list_display = ("__str__", "order", "move_up_down_links")
    ordering = ('runeword', 'order',)


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


@admin.register(Rune)
class RuneAdmin(ModelAdmin):
    form = RuneAdminForm


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
class MiscellaneousAdmin(ModelAdmin):
    form = MiscellaneousAdminForm
