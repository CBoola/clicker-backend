from django.contrib import admin

from .models import Structure, Player


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ["name", "base_prize", "production_rate"]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
