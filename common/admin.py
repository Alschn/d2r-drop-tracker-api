import json

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from import_export import resources
from import_export.widgets import JSONWidget
from jsoneditor.forms import JSONEditor

admin.site.site_header = "D2R Drop Tracker"
admin.site.site_title = "D2R Drop Tracker"

admin.site.unregister(Group)


class ModelAdmin(admin.ModelAdmin):
    """ModelAdmin where JSONField's widget is JSONEditor"""

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if isinstance(field, forms.fields.JSONField):
            field.widget = JSONEditor()
        return field


class NestedJSONWidget(JSONWidget):

    def clean(self, value, row=None, *args, **kwargs):
        try:
            return super().clean(value)
        except TypeError:
            # if value is a dictionary, turn it into json string and then load
            return json.loads(json.dumps(value))


DEFAULT_WIDGET_MAP = resources.ModelResource.WIDGETS_MAP
DEFAULT_WIDGET_MAP.update({'JSONField': NestedJSONWidget})


class ModelResourceWithNestedJSON(resources.ModelResource):
    """Model Resource which can handle nested json dictionary"""

    WIDGETS_MAP = DEFAULT_WIDGET_MAP
