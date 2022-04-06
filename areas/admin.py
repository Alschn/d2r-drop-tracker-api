from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from areas.models import Area


@admin.register(Area)
class AreaAdmin(OrderedModelAdmin):
    list_display = ('__str__', 'order', 'move_up_down_links')
    ordering = ('act', 'order',)
