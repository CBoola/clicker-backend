from django.contrib import admin

from .models import Player, Structure, Upgrade


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ["name", "base_prize", "production_rate"]


@admin.register(Upgrade)
class UpgradeAdmin(admin.ModelAdmin):
    list_display = ["name", "base_prize", "multiplier"]
