from django.contrib import admin
from django.db.models import QuerySet
from import_export.admin import ImportExportModelAdmin
from ordered_model.admin import OrderedModelAdmin

from areas.models import Area


class Level85AreaFilter(admin.SimpleListFilter):
    title = "level 85"
    parameter_name = "hell_level"

    def lookups(self, request, model_admin) -> tuple[tuple[str, str]]:
        return (
            ('85', '85'),
        )

    def queryset(self, request, queryset) -> QuerySet[Area]:
        if self.value() == "85":
            return queryset.filter(hell_level=85)


@admin.register(Area)
class AreaAdmin(ImportExportModelAdmin, OrderedModelAdmin):
    list_display = (
        '__str__',
        'normal_level', 'nightmare_level', 'hell_level',
        'order', 'move_up_down_links'
    )
    list_filter = (Level85AreaFilter, 'act')
    ordering = ('act', 'order',)
