from django.contrib import admin

from .models import Player, Structure, Upgrade, Achievement


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["name", "pk", "created_time"]
    readonly_fields = ["created_time"]
    actions = ['fix_data']

    def fix_data(self, request, queryset):
        for item in queryset:
            item.clean()
            item.save()

    fix_data.short_description = "Popraw SCHEMA'ę stanu"

class IconPreviewMixin():
    readonly_fields = ["icon_preview"]

    def icon_preview(self, obj):
        if not obj.pk:
            return "<p>Podgląd niedostępny</p>"

        return "<img src='{0}' height='200px' />".format(obj.icon.url)

    icon_preview.short_description = 'Podgląd ikony'
    icon_preview.allow_tags = True


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin, IconPreviewMixin):
    list_display = ["name", "base_prize", "production_rate"]
    readonly_fields = ["icon_preview"]


@admin.register(Upgrade)
class UpgradeAdmin(admin.ModelAdmin, IconPreviewMixin):
    list_display = ["name", "base_prize", "multiplier"]
    readonly_fields = ["icon_preview"]


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin, IconPreviewMixin):
    list_display = ["name", "type"]
    readonly_fields = ["icon_preview"]
