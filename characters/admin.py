from django.contrib import admin

from .models import Character
from common.admin import ModelAdmin


@admin.register(Character)
class CharacterAdmin(ModelAdmin):
    list_display = (
        'name', 'level', 'char_class', 'expansion',
        'hardcore', 'ladder', 'owner'
    )
