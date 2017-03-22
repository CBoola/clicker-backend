from django.contrib import admin

from .models import Structure


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ["name", "base_prize", "production_rate"]
