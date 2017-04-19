from django.contrib import admin

from .models import Player, Structure, Upgrade


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    actions = ['fix_data']

    def fix_data(self, request, queryset):
        for item in queryset:
            item.clean()
            item.save()

    fix_data.short_description = "Popraw SCHEMA'ę stanu"

@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ["name", "base_prize", "production_rate"]


@admin.register(Upgrade)
class UpgradeAdmin(admin.ModelAdmin):
    list_display = ["name", "base_prize", "multiplier"]
