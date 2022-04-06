from django import forms
from django.contrib import admin

from common.admin import ModelAdmin
from finds.models import ItemFind


class ItemFindAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['item'].label = 'Item'
        self.fields['item'].help_text = "Item that was found"
        self.fields['found_on_players'].help_text = "How many players were present in a game"
        self.fields['sold_for'].help_text = "d2jsp forum gold"

    class Meta:
        model = ItemFind
        fields = "__all__"


@admin.register(ItemFind)
class ItemFindAdmin(ModelAdmin):
    form = ItemFindAdminForm
    list_display = (
        '__str__',
        'found_by', 'found_in', 'found_on_difficulty',
        'found_on_players', 'found_at',
        'sold_for', 'sold_at',
    )
