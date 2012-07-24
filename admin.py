from django.contrib import admin
from freetext.models import FreeText

class FreeTextAdmin(admin.ModelAdmin):
    """
    Admin for FreeText model.
    """
    list_display = ('key', 'content', 'active')
    search_fields = ('key', 'content')

admin.site.register(FreeText, FreeTextAdmin)
