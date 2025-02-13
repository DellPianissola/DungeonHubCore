from django.contrib import admin


class NatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'points', 'description', 'image')
    search_fields = ('name', 'description')
    list_filter = ('points',)
    ordering = ('name',)