from django.contrib import admin


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'damage', 'description')
    search_fields = ('name', 'damage')
    list_filter = ('damage',)
    ordering = ('name',)