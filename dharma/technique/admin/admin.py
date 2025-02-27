from django.contrib import admin


class TechniqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'xp_cost', 'type', 'requirements', 'effect', 'description')
    search_fields = ('name', 'xp_cost', 'type', 'requirements', 'effect')
    list_filter = ('xp_cost',)
    ordering = ('name',)