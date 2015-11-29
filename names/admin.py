from django.contrib import admin
from names.models import Name

class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'used',)
    list_filter = ('used',)
admin.site.register(Name, NameAdmin)
