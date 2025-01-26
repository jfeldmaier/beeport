from django.contrib import admin

# Register your models here.

from .models import Stoecke, Entry

class BeeportAdmin(admin.ModelAdmin):
    fieldsets = [
            ("URL", {"fields":["stock_slug"]})
        ]

# admin.site.register(Stoecke, BeeportAdmin)
admin.site.register(Stoecke)
admin.site.register(Entry)
