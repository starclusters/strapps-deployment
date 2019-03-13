from django.contrib import admin
from biditem.models import Biditem
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Biditem)

@admin.register(Biditem)
class BiditemAdmin(ImportExportModelAdmin):
    pass
